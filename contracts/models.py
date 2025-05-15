from django.db import models
from customers.models import Customer
from products.models import Products
# Create your models here.
class Contracts(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    contract_number = models.CharField(max_length=50, unique=True, blank=False, null=False)
    contractor = models.ManyToManyField(Customer, related_name="contracts")
    site_name = models.CharField(max_length=200, blank=True, null=True, help_text='Optional')
    project_name = models.CharField(max_length=500, blank=True, null=True, help_text='Optional')
    lot_number = models.CharField(max_length=50, blank=True, null=True, help_text='Optional')
    payment_type = [
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
        ('CHEQUE', 'Cheque'),
        ('LC', 'Letter of Credit'),
        ('OTHER', 'Other'),
    ] 
    payment_method = models.CharField(max_length=10, choices=payment_type, blank=False, null=False)
    contract_value = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    contract_products = models.ManyToManyField(Products, related_name="contracts")
    credit_days = models.IntegerField(blank=False, null=False)
    contract_currency = models.CharField(max_length=10, blank=False, null=False)
    sign_date = models.DateField(blank=False, null=False)
    contract_status = [
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=contract_status, default='ACTIVE', blank=False, null=False)
    contract_start_date = models.DateField(blank=False, null=False)
    contract_end_date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_name