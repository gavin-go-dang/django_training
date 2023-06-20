from django.urls import path, include
from .views import HomeView, MyLoginView, LogoutView, MyLogoutView, RegisterView, RegisterFormView, RegisterMetaFormView, CustomUserViewSet, UserLoginAPIView, UserRegisterationAPIView

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('registerForm/', RegisterFormView.as_view(), name='registerForm'),
    path('registerMetaForm/', RegisterMetaFormView.as_view(), name='registerForm'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include(router.urls)),
    path('loginAPI/', UserLoginAPIView.as_view(), name='login-user'),
    path('RegisterAPI/', UserRegisterationAPIView.as_view(), name='register-user'),
    path('', HomeView.as_view(), name='home'),
]