from django.core import validators
from django import forms
from .models import BlogList, Registration
from django.contrib.auth.models import User  
from django import forms
from django.forms import fields

# from .models import UserInfo
class BlogCreate(forms.ModelForm):
    class Meta:
        model = BlogList
        fields = ['title', 'dtm', 'aname', 'text']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'dtm' : forms.TextInput(attrs={'class' : 'form-control'}),
            'aname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'text' : forms.TextInput(attrs={'class' : 'form-control'}),  
        }
        

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }

   
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['fname', 'lname', 'pnmbr', 'address']
        widgets = {
            'fname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'lname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'pnmbr' : forms.TextInput(attrs={'class' : 'form-control'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control'}),            
        }
        
        
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

