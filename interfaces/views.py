from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from infrastructure.repository.colisRepo import DjangoColisRepository
from infrastructure.repository.livreurRepo import DjangoLivreurRepository

from application.use_case.colisUsecase.FinaliserLivraisonUseCase import FinaliserLivraisonUseCase
from application.use_case.colisUsecase.RecupererColisUseCse import RecupererColisUseCase

class RecupererColisView(APIView):
    def post(self, request, colis_id):
        livreur_id = request.data.get('livreur_id')
        
        repo_colis = DjangoColisRepository()
        repo_livreur = DjangoLivreurRepository()
        use_case = RecupererColisUseCase(repo_colis, repo_livreur)
        
        try:
            use_case.execute(colis_id=colis_id, livreur_id=livreur_id)
            return Response({"status": "Success", "message": "Colis récupéré et livreur occupé."}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"status": "Error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    

class FinaliserLivraisonView(APIView):
    def post(self, request, colis_id):
        repo_colis = DjangoColisRepository()
        repo_livreur = DjangoLivreurRepository()
        use_case = FinaliserLivraisonUseCase(repo_colis, repo_livreur)
        
        try:
            use_case.execute(colis_id=colis_id)
            return Response({"status": "Success", "message": "Livraison terminée et livreur libéré."}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"status": "Error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
