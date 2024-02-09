from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

class FormLogin(forms.Form):
    usuario = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'form-control'}))
    password = forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'form-control'}))
    email = forms.EmailField(max_length=60,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    password1 = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))
    password2 = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Repetición Password','class':'form-control'}))
    first_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    last_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Apellido','class':'form-control'}))
    class Meta:
        model = User
        #exclude = ("date_joined")
        #fields = '__all__'
        fields= ['username','email','password1','password2','first_name','last_name']
        #help_text = {k:"" for k in fileds}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=60,widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    password1 = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))
    password2 = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':'Repetición Password','class':'form-control'}))
    first_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    last_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Apellido','class':'form-control'}))
    class Meta:
        model = User
        #exclude = ("date_joined","password","username")
        fields= ['email','password1','password2','first_name','last_name']
        #help_text = {k:"" for k in fileds}