from django import forms
from . import models

class AddPackage(forms.Form):
    trackid = forms.CharField(max_length=50,label='Трек')
    desc = forms.CharField(max_length=256,label='Комментарий')