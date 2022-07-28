from django.urls import path
from .views import MathGameView,ScoreMathGameView ,MathGameDetailView,ScoreMathCreateView
from math_game.views import ScoreMathForm
from .views import *
  
app_name = 'math_game'

urlpatterns = [
    path('math-game-main', MathGameView.as_view(), name='math-game-main'),
    path('math-game-main/<int:pk>/', MathGameDetailView.as_view(), name='detail'),
    path('math-score', ScoreMathGameView.as_view(), name='math-score'),
    path('math-game-main/create/', ScoreMathCreateView.as_view(),name='create'),
    path('',ScoreMathForm, name ='scoreMathForm'),
   
]