from django_filters.filterset import FilterSet
from .models import *

class Shipping_Address_Filter(FilterSet):

    class Meta:
        model=Shipping_Address
        fields=['id', 'customer']