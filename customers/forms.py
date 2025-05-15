from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'name_in_short', 'TIN', 'VRN', 'contact_person', 'phone', 'emial', 'address_line1', 'address_line2', 'business_type']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'name_in_short': forms.TextInput(attrs={'class': 'form-control'}),
        #     'TIN': forms.TextInput(attrs={'class': 'form-control'}),
        #     'VRN': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'emial': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'address': forms.Textarea(attrs={'class': 'form-control'}),
        #     'business_type': forms.Select(attrs={'class': 'form-control'}),
        # }