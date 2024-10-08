from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Product
from .models import customer
User = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2", "address", "phone")

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = customer
        fields = ['name', 'address', 'phone', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        customer = super(UserProfileForm, self).save(commit=False)
        customer.user.email = self.cleaned_data['email']
        if commit:
            customer.user.save()
            customer.save()
        return customer