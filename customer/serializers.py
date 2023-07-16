from rest_framework.serializers import ModelSerializer
from e_commerce_backend_system.customs import ComplexSerializer, PrimaryKeyRelatedField
from .models import *

class Women_Department_Preference_Serializer(ComplexSerializer):
    class Meta:
        model=Women_Department_Preference
        fields=["hips", "shoes_width"]

class Men_Department_Preference_Serializer(ComplexSerializer):
    class Meta:
        model=Men_Department_Preference
        fields=["chest", "shoes_width"]

class Department_Preference_Serializer(ComplexSerializer):
    men_department = Men_Department_Preference_Serializer(required=False)
    women_department = Women_Department_Preference_Serializer(required=False)

    class Meta:
        model=Department_Preference
        fields=['shoulders', 'waist', 'legs', 'shoes_size', 'top_style_size', 'bottom_style_size_waist', 'bottom_style_size_inseam', 'men_department', 'women_department']

class Customer_Serializer(ComplexSerializer):
    member = PrimaryKeyRelatedField(queryset=Member.objects.all(), required=False)
    department_preference = Department_Preference_Serializer(required=False)
    class Meta:
        model=Customer
        fields=["member", "preferred_department", "height", "weight_min", "weight_max", "age_min", "age_max", "department_preference"]