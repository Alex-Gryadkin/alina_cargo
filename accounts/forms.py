from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.utils.translation import gettext_lazy as lazy
from . import models
from django.contrib.auth.models import User




class AuthForm(AuthenticationForm):

    username = UsernameField(min_length=10, max_length=10, widget=forms.TextInput(attrs={"autofocus": True,
                                                                                         'class': 'form-control',
                                                                                         'type': 'tel',
                                                                                         'placeholder': 'Номер телефона'}))
    password = forms.CharField(
        label=lazy("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control'}),
    )
    error_messages = {
        'invalid_login': lazy(
            'Пожалуйста, проверьте корректность введенного номера телефона и пароля. Обратите внимание '
            ', эти поля чувствительны к регистру'
        )
    }


class RegisterForm(UserCreationForm):

    username = forms.CharField(min_length=10, max_length=10, widget=forms.TextInput(attrs={"autofocus": True,
                                                                                         'class': 'form-control',
                                                                                         'type': 'tel',
                                                                                         'placeholder': 'Номер телефона'}))
    full_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={"autofocus": True,
                                                                                         'class': 'form-control',
                                                                                         'type': 'tel',
                                                                                         'placeholder': 'Введите ваше имя и фамилию'}))
    city = forms.ChoiceField(choices=models.Cities.City.choices, label='Выберите город доставки товаров')

