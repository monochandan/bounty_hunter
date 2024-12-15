from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name = 'home'), # home page
    path('submit/', views.submit_story, name = 'submit_story'), # Story submission form
]