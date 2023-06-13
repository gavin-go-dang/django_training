from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
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
        return render(request, self.template_name)
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if CustomUser.objects.filter(username = username):
                messages.info(request, 'Your name has existed')
                return redirect('register')
            
            elif CustomUser.objects.filter(email = email):
                messages.info(request, 'Your email has been used')

                return redirect(register)
            
            else:
                user = CustomUser.objects.create_user(username=username, password=password, 
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('register')