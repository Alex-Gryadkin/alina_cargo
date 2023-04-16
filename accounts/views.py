from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import AuthForm, RegisterForm
from django.contrib.auth.models import User
import random
from sms.smsc_api import *


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
    if request.POST.get('username') and request.POST.get('out_otp'):
        out_otp = request.POST.get('out_otp')
        username = request.POST.get('username')
        in_otp = request.POST.get('in_otp')
        if in_otp == out_otp:
            return render(request, 'other_user_info.html', {'add_info_form': form,
                                                            'username': username})
        else:
            # add error - otp is incorrect (errors variable and sent in context)
            return render(request, 'OTP_input.html', {'username': username,
                                                      'out_otp': out_otp})

    if request.POST.get('username'):
        username = request.POST.get('username')
        profile = User.objects.filter(username=username)
        if profile.exists():                                             # change to 'no'
            out_otp = random.randint(100000, 999999)
            # add aoutofield in OTPstorage model (datetime)
            sms = SMSC()
            sms.send_sms(f'7{username}', f'Проверочный код: {out_otp}')  # !!! refreshing the page resends OTP
            return render(request, 'OTP_input.html', {'username': username,
                                                      'out_otp': out_otp})  # !!! out_otp is visible in html code

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




