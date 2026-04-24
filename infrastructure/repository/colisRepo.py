from domain.Irepository import IColisRepository
from domain.entity import Colis
from infrastructure.models import ColisModel

class DjangoColisRepository(IColisRepository):
    
    def get_by_id(self, colis_id: int) -> Colis:
        obj = ColisModel.objects.filter(id=colis_id).first()
        if not obj:
            return None
        return Colis(
            id=obj.id, 
            designation=obj.designation, 
            statut=obj.statut, 
            livreur_id=obj.livreur_id
        )

    def update(self, colis: Colis) -> Colis:
        
        ColisModel.objects.filter(id=colis.id).update(
            statut=colis.statut,
            livreur_id=colis.livreur_id
        )
        return colis

    def list_by_status(self, statut: str) -> list[Colis]:
        query = ColisModel.objects.filter(statut=statut)
        return [
            Colis(id=obj.id, designation=obj.designation, statut=obj.statut, livreur_id=obj.livreur_id)
            for obj in query
        ]