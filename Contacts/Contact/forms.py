from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class PersonForm2(forms.ModelForm):
    name = forms.CharField(required=False)
    dob = forms.DateField(required=False)
    email = forms.EmailField(required=False)
    mobile = forms.CharField(required=False)
    dp_pic = forms.ImageField(required=False)
    class Meta:
        model = Person
        fields = '__all__'