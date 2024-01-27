from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUp_From(forms.ModelForm):
    username=forms.CharField(label='Your Username',widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    email=forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}))
    user_type=forms.Select(attrs={'class':'form-control form-control-lg'})
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))
    

    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2','user_type']
    
    
        
class SignIn_Form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Enter Email'
            })
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 'placeholder': 'Enter Password'
            })
        )

class Profile_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','age','address','family_member_count']
        widget = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'age': forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'family_member_count': forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
        }