from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class UserInfoForm(forms.Form):
    dietary_restrictions = forms.CharField(max_length=100, required=False)
    food_allergies = forms.CharField(max_length=100, required=False)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    preferred_breakfast_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    preferred_lunch_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    preferred_dinner_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
