from domain.Irepository import ILivreurRepository
from domain.entity import Livreur
from infrastructure.models import LivreurModel

class DjangoLivreurRepository(ILivreurRepository):
    
    def get_by_id(self, livreur_id: int) -> Livreur:
        obj = LivreurModel.objects.filter(id=livreur_id).first()
        if not obj:
            return None
        return Livreur(
            id=obj.id, 
            nom=obj.nom, 
            disponible=obj.disponible, 
            vehicule=obj.vehicule
        )

    def update_disponibilite(self, livreur_id: int, disponible: bool) -> None:
        LivreurModel.objects.filter(id=livreur_id).update(disponible=disponible)