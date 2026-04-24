from django.db import models


#Table cdu client
class ClientModel(models.Model):
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20, unique=True)
    adresse = models.TextField()

    def __str__(self):
        return self.nom



#table du livreur
class LivreurModel(models.Model):
    nom = models.CharField(max_length=255)
    vehicule = models.CharField(max_length=100)
    est_disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom




#Tble du clois
class ColisModel(models.Model):
    STATUT_CHOICES = [
        ('PENDING', 'En attente'),
        ('IN_PROGRESS', 'En cours'),
        ('DELIVERED', 'Livré'),
    ]
    
    description = models.TextField()
    poids = models.FloatField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='PENDING')
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name='colis')
    livreur = models.ForeignKey(LivreurModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Colis {self.id} - {self.statut}"