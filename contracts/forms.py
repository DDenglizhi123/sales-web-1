from django import forms
from .models import Contracts

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ['contractor', 'contract_number', 'site_name', 'project_name', 'lot_number', 'contract_value', 'payment_method', 'credit_days', 'contract_currency', 'sign_date', 'contract_end_date']
        
        
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