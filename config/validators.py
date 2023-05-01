from django.core.exceptions import ValidationError
from django.utils.translation import gettext as txt


class LengthValidator:
    """
    Validate a password length.
    """
    def __init__(self, length=6,):
        self.length = length

    def validate(self, password, user=None):
        if len(password) < self.length:
            raise ValidationError(
                txt("Пароль должен состоять минимум из 6 символов"),
                code='password_minimum_6'
            )

    def get_help_text(self):
        return txt(
            "Пароль должен состоять минимум из 6 символов."
        )


class NumAndAlphaPasswordValidator:
    """
    Validate that the password is not entirely numeric or alphabetical.
    """
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                txt("Пароль должен также содержать буквы a-z"),
                code="password_entirely_numeric"
            )
        if password.isalpha():
            raise ValidationError(
                txt("Пароль должен также содержать цифры 0-9"),
                code="password_entirely_alpha"
            )

    def get_help_text(self):
        return txt("Пароль должен состоять из цифр и латинских букв (a-z)")
