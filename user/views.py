from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from e_commerce_backend_system.customs import generate_code_with_email, decode_code
from django.core.mail import EmailMessage
from .models import Recover_Code


from django.core.mail import send_mail


from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = Member.objects.get(email=obj)
        return user.pk == int(view.kwargs['pk'])



class MemberView(ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer

    @action(detail=False, methods=['POST'], serializer_class=Recover_Password_Serializer)
    def recover_password(self, request, *args, **kwargs):
        data = request.data
        email = data['email']

        code = generate_code_with_email(email)

        Recover_Code.objects.create(code=code)

        subject = 'Recover password'
        body = f'please follow this link to reset your password http://127.0.0.1:8000/reset_password/{code}/'
        from_email = "worksmy147@gmail.com"
        to_email = [f'{email}']

        send_mail(subject=subject, message=body, from_email=from_email, recipient_list=to_email)
       

        return Response("Email Sent")

    @action(detail=True, methods=['POST'])
    def reset_password(self, request, pk=None, **kwargs):
        data = request.data
        if Recover_Code.objects.filter(code=pk).count() != 0:
            decoded_token = decode_code(pk)
            email = decoded_token['email']
            password = data['password']
            
            member = Member.objects.get(email=email)
            member.objects.set_password(password)
            member.save()

            return Response({"message": "Password changed"})
        
        return Response({"message": "code is not valid"})


    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [HasAPIKey]
        elif self.action == 'destroy' or self.action == 'update':
            permission_classes = [HasAPIKey, IsAdminUser, IsAccountOwner]
        elif self.action == 'list':
            permission_classes = [HasAPIKey, IsAdminUser]
        elif self.action == 'recover_password':
            permission_classes = [HasAPIKey]
        else:
            permission_classes = [HasAPIKey, IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]
    
