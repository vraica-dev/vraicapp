from .models import CVDocument
from rest_framework import serializers


class CVDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVDocument
        fields = [
            '__all__'
        ]

