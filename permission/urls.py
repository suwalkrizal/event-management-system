from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
   path('register/', RegistrationAPIView.as_view(), name='user-registration'),
   path('login/', LoginAPIView.as_view(), name='user-login'),
   path('logout/', LogoutAPIView.as_view(), name='user-logout'),
]