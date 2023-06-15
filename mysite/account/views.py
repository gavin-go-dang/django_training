from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework import viewsets, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import CustomUserSerializer, UserLoginSerializer, UserRegisterationSerializer
from .forms import SignUpForm, RegisterMetaForm


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'    
    

class MyLogoutView(LogoutView):
    next_page = 'home'


class MyLoginView(LoginView):
    template_name = 'login.html'
    success_url = ''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('home')


class RegisterView(View):
    template_name = 'registeration.html'


    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username):
                messages.info(request, 'Your name has existed')
                return redirect('register')
            
            elif CustomUser.objects.filter(email=email):
                messages.info(request, 'Your email has been used')

                return redirect(register)
            
            else:
                user = CustomUser.objects.create_user(username=username, password=password, 
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')


class RegisterFormView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'registerform.html')

    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            form = SignUpForm()
            context = {'form' : form}
            return render(request, 'registerform.html', context)

        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        user = CustomUser.objects.create_user(username=username, password=password,         
                                        email=email, first_name=first_name, last_name=last_name)

        return redirect('login')



class RegisterMetaFormView(View):
    def post(self, request):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'registerform.html', {'form': form})

        else:
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = CustomUser.objects.create_user(username=username, password=password,         
                                            email=email, first_name=first_name, last_name=last_name)
                                            
            return redirect('login')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'registerform.html')


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

User = get_user_model()


class UserLoginAPIView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer_context = {
            'request': request,
        }
            user = serializer.validated_data
            serializer = CustomUserSerializer(user, context=serializer_context)
            token = RefreshToken.for_user(user)
            data = serializer.data
            data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
            return redirect('home')


class UserRegisterationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterationSerializer


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return redirect()
