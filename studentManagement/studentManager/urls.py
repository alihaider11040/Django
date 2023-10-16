from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_results/', views.send_results, name='send_results'),
]
