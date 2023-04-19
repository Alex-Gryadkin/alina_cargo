from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import AuthForm, RegisterForm
from django.contrib.auth.models import User
from . models import OTPStorage, CargoUser, Cities
import random
from sms.smsc_api import *
import datetime


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
        username = request.POST.get('username')
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            city = Cities.objects.get(city=form.cleaned_data.get('city'))
            user = form.save()
            user_id = user.id
            cargo_code = f'WINWIN-{city}{user_id}'
            cargouser = CargoUser(username=user, full_name=full_name, city=city, cargo_code=cargo_code)
            cargouser.save()
            login(request, user)
            return redirect('packages:list')

        return render(request, 'final_creation.html', {'form': form,
                                                       'username': username})

    if request.GET.get('username') and request.GET.get('in_otp'):
        username = request.GET.get('username')
        out_otp = OTPStorage.objects.get(phone=username).otp
        in_otp = request.GET.get('in_otp')
        if in_otp == out_otp:
            return render(request, 'final_creation.html', {'form': form,
                                                           'username': username})
        else:
            otp_error = "Код не совпадает"
            return render(request, 'OTP_input.html', {'username': username,
                                                      'error': otp_error})

    elif request.GET.get('username'):
        username = request.GET.get('username')
        profile = User.objects.filter(username=username)
        if not profile.exists():
            try:
                otp_session = OTPStorage.objects.get(phone=username)
            except OTPStorage.DoesNotExist:
                otp_session = None
            if otp_session:

                otp_session_created = otp_session.date_added
                now = datetime.datetime.now(otp_session_created.tzinfo)
                time_delta = datetime.datetime.timestamp(now) - datetime.datetime.timestamp(otp_session_created)

                if time_delta > 60:
                    out_otp = random.randint(100000, 999999)
                    otp_session.date_added = now
                    otp_session.otp = out_otp
                    otp_session.save()
                    sms = SMSC()
                    sms.send_sms(f'7{username}', f'Проверочный код: {out_otp}')
                    return render(request, 'OTP_input.html', {'username': username})

                else:
                    return render(request, 'OTP_input.html', {'username': username})

            else:
                out_otp = random.randint(100000, 999999)
                otp_session = OTPStorage(phone=username, otp=out_otp)
                otp_session.save()
                sms = SMSC()
                sms.send_sms(f'7{username}', f'Проверочный код: {out_otp}')
                return render(request, 'OTP_input.html', {'username': username,
                                                          'out_otp': out_otp})  # later - delete out_otp
        else:
            user_exist_error = 'Пользователь с таким номером уже зарегистрирован'
            return render(request, 'register.html', {'form': form,
                                                     'error': user_exist_error})

    return render(request, 'register.html', {'form': form})



# def password_reset(request):
#     if request.method == 'POST':
#         form = OTPInput(data=request.POST)
#         if form.is_valid():
#             pass
#     else:
#         form = OTPInput()
#     return render(request, 'otp_input.html', {'form': form})




