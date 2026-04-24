from abc import ABC, abstractmethod
from typing import List, Optional
from .entity import Client, Livreur, Colis

#Les contrats de l'entité client
class IClientRepository(ABC):
    @abstractmethod
    def save(self, client: Client) -> Client:
        pass

    @abstractmethod
    def get_all(self) -> List[Client]:
        pass

    @abstractmethod
    def get_by_id(self, client_id: int) -> Optional[Client]:
        pass


#Les contrats du livreur
class ILivreurRepository(ABC):
    @abstractmethod
    def save(self, livreur: Livreur) -> Livreur:
        pass

    @abstractmethod
    def get_all(self) -> List[Livreur]:
        pass

    @abstractmethod
    def get_by_id(self, livreur_id: int) -> Optional[Livreur]:
        pass


#Les contraaat s du colis
class IColisRepository(ABC):
    @abstractmethod
    def save(self, colis: Colis) -> Colis:
        pass

    @abstractmethod
    def get_all(self) -> List[Colis]:
        pass

    @abstractmethod
    def get_by_id(self, colis_id: int) -> Optional[Colis]:
        pass