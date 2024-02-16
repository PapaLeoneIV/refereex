from django.urls import path
from . import views

urlpatterns = [
    path('leagues/', views.get_leagues, name='leaguelist'),
    path('leagues/<int:pk>', views.get_teams, name='teamlist'),
]