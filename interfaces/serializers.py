from rest_framework import serializers

class ClientSerializer(serializers.Serializer):
    # On définit les champs manuellement pour ne pas dépendre du modèle Django
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    telephone = serializers.CharField(max_length=20)
    adresse = serializers.CharField()



class LivreurSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    vehicule = serializers.CharField(max_length=100)
    disponible = serializers.BooleanField(default=True)


class ColisSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    designation = serializers.CharField(max_length=255)
    poids = serializers.FloatField()
    statut = serializers.CharField(read_only=True) 
    
    client_id = serializers.IntegerField(write_only=True)
    livreur_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    
    