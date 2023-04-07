from django import forms
from . import models
class AddPackage(forms.Form):
    trackid = forms.CharField(max_length=50, label='Номер трека')
    desc = forms.CharField(help_text="Можно добавить описание", widget=forms.Textarea, required=False, label='Описание')


