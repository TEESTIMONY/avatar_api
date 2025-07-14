from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Avatar

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'
        extra_kwargs = {
            'svg_data': {'read_only': True},  # Tell DRF this is generated, not input
            'part':{'read_only':True}
        }

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            # Try authenticating with email
            try:
                user_obj = User.objects.get(email=username)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        data['user'] = user
        return data
