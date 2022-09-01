from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style = {'input_type': 'password'} ,write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        #django already contains username, email and password so we need to define password2
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    #overriding self method to solve extra password field error
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'Error': 'Passwords do not match'})
        
        if User.objects.filter(email= self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error': 'Email already exits'})
            
        account = User(email= self.validated_data['email'], username= self.validated_data['username'])
        account.set_password(self.validated_data['password'])
        account.save()
        
        return account