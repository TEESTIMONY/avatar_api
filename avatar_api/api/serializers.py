from rest_framework import serializers
from .models import Avatar

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'
        extra_kwargs = {
            'svg_data': {'read_only': True},  # Tell DRF this is generated, not input
            'part':{'read_only':True}
        }
