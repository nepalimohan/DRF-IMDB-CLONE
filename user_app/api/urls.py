from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token #drf provides default params for login

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
]