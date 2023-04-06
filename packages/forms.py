from django import forms
from . import models
class AddPackage(forms.ModelForm):
    trackid = forms.CharField(max_length=50, label='Номер трека')
    class Meta:
        model = models.UserPackages
        fields = ['desc']

        widgets = {
            'desc': forms.TextInput(attrs={'class': 'form-control'})
        }
