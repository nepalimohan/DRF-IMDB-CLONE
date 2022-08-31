from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style = {'input_type': 'password'} ,write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        #django already contains username, email and password so we need to define password2
        extra_kwargs = {
            'password': {'wtrite_only': True}
        }