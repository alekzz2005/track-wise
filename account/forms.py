# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# 1. Custom Registration Form
class CustomUserCreationForm(UserCreationForm):
    # Add any extra fields here if needed (e.g., first_name, last_name)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields # Or specify custom fields like ('username', 'email', 'password')

# 2. Custom Login Form (often kept simple)
class CustomAuthenticationForm(AuthenticationForm):
    # You can add custom styling or validation here
    pass