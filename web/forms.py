from django import forms
from .models import obj

class signupForm(forms.Form):
    name=forms.CharField(label='name',max_length=20)
    username=forms.CharField(label='username',max_length=20)
    password=forms.CharField(label='password',max_length=20)

class CreateequipmentForm(forms.ModelForm):
    
    class Meta:
        model = obj
        fields = ['name', 'date_s', 'date_e', 'category']
        widgets={
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'date_s': forms.DateInput(attrs= {'class': 'form-control'}),
            'date_e': forms.DateInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'}),
        }