from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
from event.permission import isAdminReadOnly

# Create your views here.
class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise AuthenticationFailed('Both username and password are required')
        
    
        user = authenticate(request, username=username, password=password)
        if user:
            
            if not user.is_active:
                raise AuthenticationFailed('User account is inactive')
            

            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        
        raise AuthenticationFailed('Invalid username or password')
    

class LogoutAPIView(APIView):
   permission_classes = [IsAuthenticated]
   def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      if not(username and password):
         return Response({'detail':'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
      user = authenticate(username=username, password=password)
      if user is not None:
         logout(request)
         try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response({'detail': 'Successfully logged out.'})
         except Token.DoesNotExist:
            return Response({'detail': 'Token does not exist.'}, status=status.HTTP_404_NOT_FOUND)
      else:
         return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)