from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User,PasswordEntry
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class PasswordEntryForm(ModelForm):
    class Meta:
        model=PasswordEntry
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields=['website','website_user_name','password','additional_info']
        
        

