from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['number', 'name', 'width', 'height', 'depth', 'style', 'material', 'year_created',
                  'origin', 'condition', 'purchase_price', 'sale_price',
                  'is_available_for_sale', 'image', 'status', 'description']
