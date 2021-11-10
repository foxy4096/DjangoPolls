from django import forms
from django.contrib.auth.models import User

class SimplifiedUserChangeForm(forms.ModelForm):
    """
    A Simplified user form with only required fields
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
