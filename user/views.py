from rest_framework.viewsets import ModelViewSet
from .serializers import *

class MemberView(ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer