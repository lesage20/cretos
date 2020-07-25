from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):


    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
    }))

    tel = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail',
    }))

    

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100',
        'placeholder': 'Message',
        'id': 'message',
        'cols': '30',
        'rows': '9',
    }))

    class Meta:
        model = Contact
        fields = ['message', 'nom', 'email', 'tel']
