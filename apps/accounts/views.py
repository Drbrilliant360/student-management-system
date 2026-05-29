from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from .models import User


class LoginView(View):
    template_name = 'accounts/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        next_url = request.GET.get('next', '')
        return render(request, self.template_name, {'next': next_url})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            # If next_url is provided and safe, use it
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            
            # Otherwise redirect based on user role
            if user.role == 'student':
                return redirect('student:dashboard')
            elif user.role == 'staff':
                return redirect('staff:dashboard')
            elif user.role == 'admin':
                return redirect('admin_panel:dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
        
        return render(request, self.template_name, {'next': next_url})


class StaffLoginView(View):
    template_name = 'accounts/staff_login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.role == 'staff':
                return redirect('staff:dashboard')
            return redirect('home')
        next_url = request.GET.get('next', '')
        return render(request, self.template_name, {'next': next_url})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.role != 'staff':
                messages.error(request, 'This login is for staff members only.')
                return render(request, self.template_name, {'next': next_url})
            
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            
            # If next_url is provided and safe, use it
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            
            return redirect('staff:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
        
        return render(request, self.template_name, {'next': next_url})


class SignupView(View):
    template_name = 'accounts/signup.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, self.template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, self.template_name)
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role='student'
        )
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('accounts:login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('accounts:login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
