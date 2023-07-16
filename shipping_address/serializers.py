from rest_framework.serializers import ModelSerializer
from e_commerce_backend_system.customs import ComplexSerializer, PrimaryKeyRelatedField
from .models import *
from customer.models import Customer

class Day_Availability_Serializer(ComplexSerializer):
    class Meta:
        model=Day_Availability
        fields=['day', 'start_at', 'stop_at']

class Delivery_Instruction_Serializer(ComplexSerializer):
    address_availability = Day_Availability_Serializer(many=True, required=False)

    class Meta:
        model=Delivery_Instructions
        fields=['property_type', 'leave_at', 'address_availability', 'recieve_on_federal_holidays', 'security_code', 'call_box', 'key_required', 'additional_instructions']

class Shipping_Address_Serializer(ComplexSerializer):
    customer = PrimaryKeyRelatedField(queryset=Customer.objects.all(), required=False)
    delivery_instructions = Delivery_Instruction_Serializer(required=False)
    class Meta:
        model=Shipping_Address
        fields=['id', 'customer', 'country', 'full_name', 'phone_number', 'address', 'city', 'state', 'zip_code', 'delivery_instructions']