from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['item_number', 'item_name', 'product_type', 'unit', 'price', 'stock_quantity', 'weight_in_kg', 'item_number']
