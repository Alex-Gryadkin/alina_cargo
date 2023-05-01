from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.utils.translation import gettext_lazy as lazy
from .models import Cities


class AuthForm(AuthenticationForm):
    username = UsernameField(min_length=10,
                             max_length=10,
                             widget=forms.TextInput(attrs={"autofocus": True,
                                                           'class': 'form-control',
                                                           'type': 'tel',
                                                           'placeholder': 'Номер телефона'}))
    password = forms.CharField(
        label=lazy("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Пароль'}),
    )
    error_messages = {
        'invalid_login': lazy(
            'Пожалуйста, проверьте корректность введенного номера телефона и пароля. Обратите внимание'
            ', эти поля чувствительны к регистру.'
        )
    }


class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=10,
                               max_length=10,
                               widget=forms.TextInput(attrs={"autofocus": True,
                                                             'class': 'form-control',
                                                             'type': 'tel',
                                                             'placeholder': 'Номер телефона'}))
    full_name = forms.CharField(max_length=40,
                                label='Ваши имя и фамилия',
                                widget=forms.TextInput(attrs={"autofocus": True,
                                                              'class': 'form-control',
                                                              'type': 'tel',
                                                              'placeholder': 'Ваши имя и фамилия'}))
    city = forms.ModelChoiceField(queryset=Cities.objects,
                                  label='Выберите город доставки грузов',
                                  widget=forms.Select(attrs={'class': 'form-select'}),
                                  empty_label="Город не выбран")

    password1 = forms.CharField(
        label=("Придумайте пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control",
                                          'placeholder': 'Придумайте пароль'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Повторите пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control",
                                          'placeholder': 'Повторите пароль'}),
        strip=False,
        help_text=("Введите повторно тот же пароль"),
    )

    error_messages = {
        "password_mismatch": lazy("Пароли не совпадают"),
    }

