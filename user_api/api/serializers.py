from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = User
        fields = [
                  'username',  
                  'email',
                  'password',
                  'password2',
                  ]
        
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        print("-------------------------------------------------------------------1")
        password1 = self.validated_data["password"] 
        password2 = self.validated_data["password2"]
        email = self.validated_data["email"]
        
        if password1 != password2:
            print("-------------------------------------------------------------2")
            raise serializers.ValidationError("both passwords are not equal")
        
        if User.objects.filter(email = email).exists():
            print("----------------------------------------------------------------3")
            raise serializers.ValidationError("User with email already exists")
            
        account = User(username = self.validated_data["username"], email = self.validated_data["email"])
        account.set_password(password1)
        account.save()
        
        return account