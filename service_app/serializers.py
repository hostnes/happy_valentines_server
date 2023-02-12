from rest_framework import serializers

from service_app.models import Valentine, User


class ValentineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valentine
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"