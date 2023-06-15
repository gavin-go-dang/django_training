from django.urls import path
from .views import HomeView, MyLoginView, LogoutView, MyLogoutView, RegisterView, RegisterFormView, RegisterMetaFormView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('registerForm/', RegisterFormView.as_view(), name='registerForm'),
    path('registerMetaForm/', RegisterMetaFormView.as_view(), name='registerForm'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
]