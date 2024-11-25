from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 
                  'username', 
                  'role', 
                  'password'
                  ]
        extrakwargs = {'password': {'write_only': True}}
