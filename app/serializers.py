from rest_framework import serializers

from app.models import Ramais


class RamaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramais
        fields = "__all__"