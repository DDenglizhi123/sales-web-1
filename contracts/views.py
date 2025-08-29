from django.shortcuts import render
from .models import Contracts
from django.views.generic import ListView, CreateView
# Create your views here.
class ContractListView(ListView):
    model = Contracts
    template_name = 'contracts/contract_list.html'
    context_object_name = 'contracts'
    fields = ['contractor', 'contract_number', 'site_name', 'project_name', 'lot_number', 'contract_value', 'payment_method', 'credit_days', 'contract_currency', 'sign_date', 'contract_start_date', 'contract_end_date']
    paginate_by = 10  # Number of customers per page
class ContractCreateView(CreateView):
    pass