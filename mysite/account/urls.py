from django.urls import path
from .views import HomeView, MyLoginView, LogoutView, MyLogoutView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', MyLoginView.as_view(), name = 'login'),
    path('logout/', MyLogoutView.as_view(), name = 'logout'),
    path('', HomeView.as_view(), name = 'home')
]