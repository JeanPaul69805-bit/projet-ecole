class FinaliserLivraisonUseCase:
    def __init__(self, colis_repo: IColisRepository, livreur_repo: ILivreurRepository):
        self.colis_repo = colis_repo
        self.livreur_repo = livreur_repo

    def execute(self, colis_id: int):
        colis = self.colis_repo.get_by_id(colis_id)
        if not colis:
            raise ValueError("Colis introuvable.")
            
        if colis.statut != "EN_COURS":
            raise ValueError("Seul un colis 'En cours' peut être finalisé.")

        colis.statut = "LIVRE"
        self.colis_repo.update(colis)
        
        self.livreur_repo.update_disponibilite(colis.livreur_id, disponible=True)
        
        return colis