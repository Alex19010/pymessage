from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import User



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "date_of_birth", "email", "password", "password_confirm", "address")
    
    
    def clean(self):
        password = self.cleaned_data["password"]
        password_confirm = self.cleaned_data["password_confirm"]

        if password != password_confirm:
            raise ValidationError(message={"password":"Пароли не совпали!"}) 

        super().clean()