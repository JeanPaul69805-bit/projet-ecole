# App Livraison - Backend (Clean Architecture)

##  Prérequis
- Python 3.10 ou plus
- Git

##  Installation (Pour l'équipe)

Suivez ces étapes pour configurer le projet sur votre machine locale :

1. **Cloner le projet**
   ```bash
   git clone url du projet créer par jp
   cd app_Livraison
   ```

2. **Créer l'environnement virtuel**
    python -m venv venv

3. **Activer l'environnement virtuel**
    venv\Scripts\activate

4. **Installer les dépendances**
    pip install -r requirements.txt

5. **Configurer la base de données**
    python manage.py migrate

6. **Lancer le serveur**
python manage.py runserver


##  Pour chaque fonctionnalités, il faut:
    -aller dans **Infrastructure/Repository**, définir le Repository de la tache
    -aller dans **application/usecase**, définir le usecase de la tache
    -zinsi de suite...


##  Les diférentes taches du projet par personne

****
***Afiza***
****

1. Module "Clients" 
    CRUD complet des clients : 
        -Creér
        -Lister tous les clients
        -Recuper un client par id
 

****
***Camille***
****
2. Module "Livreurs" 
    CRUD complet des livreurs : Enregistrer les nouveaux livreurs et leurs véhicules.
        -Creér
        -Lister tous les livreurs
        -Recuper un livreur par id



****
***Judith***
****
3. Module "Colis" (Le cœur du métier)
    -Creér Créer un colis en le liant obligatoirement à un Client existant
    -Lister tous les colis
    -Recuper un colis par id



****
***Giles***
****
4. Module "Affectation & Logique" 
    Affectation manuelle : Une route pour l'admin qui permet de choisir un livreur spécifique pour un colis spécifique.
    Listing des colis par statut : Voir tous les colis "En attente", "En cours" ou "Livrés".
    Vérification de règle métier : Empêcher d'affecter un livreur s'il est déjà "Indisponible".
    Mise à jour du statut : Le livreur confirme qu'il a récupéré le colis (statut passe à IN_PROGRESS) puis qu'il l'a livré (DELIVERED).
    Vérification de règle métier : Empêcher d'affecter un livreur s'il est déjà "Indisponible".
    Gestion de la disponibilité : Créer une route permettant à un livreur de passer son statut à "Disponible" ou "Indisponible" (On-duty/Off-duty).
    




