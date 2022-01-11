from authentication import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    class Meta:
        model = models.User
        fields = '__all__'
