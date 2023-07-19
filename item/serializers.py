from e_commerce_backend_system.customs import ComplexSerializer
from .models import *

class Item_Serializer(ComplexSerializer):
    class Meta:
        model=Item
        fields="__all__"
