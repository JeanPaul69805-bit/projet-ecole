
from django.urls import path
from .views import *

urlpatterns = [
    path('', ColisListView.as_view()),
    path('create/', ColisCreateView.as_view()),
    path('<int:pk>/', ColisDetailView.as_view()),
    
]