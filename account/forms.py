from django.forms import ModelForm
from django import forms
from website.models import NewsLetter
from .models import Order, Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class NewsletterForm(forms.Form, ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = ['email']
    
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = NewsLetter.objects.get(email=email)
        except NewsLetter.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
