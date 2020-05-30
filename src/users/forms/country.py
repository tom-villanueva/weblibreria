from django import forms
from users.models import Country

class Country(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'