from rest_framework import serializers

from .models import Instituition

class InstituitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituition
        fields = [
            "id",
            "name",
            "state",
            "country",
        ]