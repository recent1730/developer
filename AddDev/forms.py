from django import forms
from AddDev.models import Developer

class DeveloperForm(forms.ModelForm):
    class Meta :
        model=Developer
        fields='__all__'
