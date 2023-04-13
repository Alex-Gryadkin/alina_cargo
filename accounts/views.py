from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import AuthForm, AuthenticationForm, OTPInput, RegisterForm
from . models import CargoUser
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('packages:list')
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        user = request.POST.get('username')
        profile = User.objects.filter(username=user)
        if not profile.exists():
            city = request.POST.get('city')
            fullname = request.POST.get('fullname')
            return redirect('accounts:otpinput')
            #  add error - user already exists

    return render(request, 'register.html', {'form': form})


def otp_input_view(request):
    return render(request, 'OTP_input.html')

# def password_reset(request):
#     if request.method == 'POST':
#         form = OTPInput(data=request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = OTPInput()
#     return render(request, 'otp_input.html', {'form': form})




