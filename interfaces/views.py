
from rest_framework import generics
from infrastructure.models import ColisModel
from .serializers import ColisSerializer

class ColisCreateView(generics.CreateAPIView):
    queryset = ColisModel.objects.all()
    serializer_class = ColisSerializer
    
class ColisListView(generics.ListAPIView):
    queryset = ColisModel.objects.all().order_by('-date_creation')
    serializer_class = ColisSerializer
    
class ColisDetailView(generics.RetrieveAPIView):
    queryset = ColisModel.objects.all()
    serializer_class = ColisSerializer