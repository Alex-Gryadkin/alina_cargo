from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import AuthForm, AuthenticationForm, OTPInput


def login_view(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        form_otp = OTPInput(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('packages:list')
    else:
        form = AuthForm()
        form_otp = OTPInput()
    return render(request, 'login.html', {'form': form,
                                          'form_otp': form_otp,
                                          })

def register_view(request):
    pass


def password_reset(request):
    if request.method == 'POST':
        form = OTPInput(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = OTPInput()
    return render(request, 'OTP_input.html', {'form': form})




