from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as lazy
from . import models




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


class OTPInput(forms.Form):
    otp_code = forms.CharField(min_length=6, max_length=6)


class RegisterForm(forms.ModelForm):

    username = UsernameField(required=True,max_length=10, min_length=10, widget=forms.TextInput(attrs={"autofocus": True,
                                                                                                        'class': 'form-control',
                                                                                                        'type': 'tel',
                                                                                                        'placeholder': 'Номер телефона'}))
    fullname = UsernameField(required=True, max_length=40, widget=forms.TextInput(attrs={"autofocus": True,
                                                                                         'class': 'form-control',
                                                                                         'placeholder': 'Имя и Фамилия'}))

    class Meta:
        model = models.Cities
        fields = ['city']


