from django import forms 
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('pname','pdesc','price','photo')
        widgets = {
            'pname':forms.TextInput(attrs ={'class':'form-control'}),
            'pdesc':forms.TextInput(attrs ={'class':'form-control'}),
            'price':forms.NumberInput(attrs ={'class':'form-control'}),
        
        }
    
  