from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as lazy


class AuthForm(AuthenticationForm):

    username = UsernameField(max_length=10, min_length=10, widget=forms.TextInput(attrs={"autofocus": True,
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





