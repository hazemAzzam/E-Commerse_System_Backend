from rest_framework.viewsets import ModelViewSet
from .serializers import *
from customer.models import Member
from .filters import Shipping_Address_Filter

# Create your views here.
class Shipping_Address_View(ModelViewSet):
    queryset=Shipping_Address.objects.all()
    serializer_class=Shipping_Address_Serializer
    filterset_class = Shipping_Address_Filter
    
    def create(self, request, *args, **kwargs):
        user = Member.objects.get(email=request.user)
        request.data['customer'] = user.pk
        return super().create(request, *args, **kwargs)