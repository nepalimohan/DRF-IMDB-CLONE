from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.wavies_list, name='wavies_list'),
]
