from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import Member

class MemberSerializer(ModelSerializer):
    
    class Meta:
        model=Member
        fields="__all__"
        extra_kwargs = {
            'password' : {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        if not password:
            raise ValueError("Password cannot be null")
        
        #super().create(validated_data)
        user = Member.objects.create_user(email=email, password=password, **validated_data)

        return user
    
class Recover_Password_Serializer(Serializer):
    email = EmailField(required=True)
    password = CharField(required=False)