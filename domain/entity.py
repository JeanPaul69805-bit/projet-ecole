from dataclasses import dataclass
from typing import Optional
from enum import Enum

class StatutColis(Enum):
    PENDING = "En attente"
    IN_PROGRESS = "En cours"
    DELIVERED = "Livré"

from typing import Optional, List

class Client:
    def __init__(self, nom: str, telephone: str, adresse: str, id: Optional[int] = None):
        self.id = id
        self.nom = nom
        self.telephone = telephone
        self.adresse = adresse

class Livreur:
    def __init__(self, nom: str, vehicule: str, est_disponible: bool = True, id: Optional[int] = None):
        self.id = id
        self.nom = nom
        self.vehicule = vehicule
        self.est_disponible = est_disponible

class Colis:
    def __init__(self, description: str, poids: float, statut: str, client: Client, livreur: Optional[Livreur] = None, id: Optional[int] = None):
        self.id = id
        self.description = description
        self.poids = poids
        self.statut = StatutColis
        self.client = client
        self.livreur = livreur