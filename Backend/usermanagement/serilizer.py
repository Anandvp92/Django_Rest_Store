from rest_framework.serializers import ModelSerializer
from .models import User

class Userserializer(ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"


class Registerserializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'phonenumber']
        extra_kwargs = {'password': {'write_only': True}}  # Ensures password is write-only

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user