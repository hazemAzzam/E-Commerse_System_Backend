from rest_framework.viewsets import ModelViewSet
from .serializers import *

class Customer_View(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=Customer_Serializer

    def create(self, request, *args, **kwargs):
        user = Member.objects.get(email=request.user)
        request.data['member'] = user.pk
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        user = Member.objects.get(email=request.user)
        request.data['member'] = user.pk
        return super().update(request, *args, **kwargs)