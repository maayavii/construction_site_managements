from django import forms
from . models import Product



class EditProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','price','image']