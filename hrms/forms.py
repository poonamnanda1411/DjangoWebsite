from django import forms
from .models import Person

class empForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=["firstname","lastname","email","startdate","salary","isActive"]
