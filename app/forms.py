from django import forms
from .models import Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from app.models import Profile


# Create your forms here.

class UserRegistrationForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BusinessAddForm(forms.Form):

    class Meta:
        model = Business
        fields = ['business_name', 'business_email', 'business_phone', 'business_location', 'business_description', 'business_image']