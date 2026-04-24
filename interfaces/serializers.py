
from rest_framework import serializers
from infrastructure.models import ColisModel

class ColisSerializer(serializers.ModelSerializer):

    class Meta:
        model = ColisModel
        fields = '__all__'

    def validate_poids(self, value):
        if value <= 0:
            raise serializers.ValidationError("Poids invalide")
        return value