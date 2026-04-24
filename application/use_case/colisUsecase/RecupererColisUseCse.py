from domain.Irepository import IColisRepository, ILivreurRepository

class RecupererColisUseCase:
    def __init__(self, colis_repo: IColisRepository, livreur_repo: ILivreurRepository):
        self.colis_repo = colis_repo
        self.livreur_repo = livreur_repo

    def execute(self, colis_id: int, livreur_id: int):
        livreur = self.livreur_repo.get_by_id(livreur_id)
        if not livreur:
            raise ValueError("Livreur introuvable.")
        
        if not livreur.disponible:
            raise ValueError("Vous avez déjà une livraison en cours. Finissez-la d'abord !")

        colis = self.colis_repo.get_by_id(colis_id)
        if not colis or colis.statut != "EN_ATTENTE":
            raise ValueError("Ce colis n'est plus disponible pour ramassage.")

        colis.livreur_id = livreur_id
        colis.statut = "EN_COURS"
        
        self.colis_repo.update(colis)
        self.livreur_repo.update_disponibilite(livreur_id, disponible=False) # On occupe le livreur
        
        return colis