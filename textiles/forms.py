from django import forms
from textiles.models import Boutique, Product


class BoutiqueForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "20", 'rows': "5", }))

    class Meta:
        model = Boutique
        fields = ['name', 'caption', 'description', 'logo', 'cover_image' ]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = []