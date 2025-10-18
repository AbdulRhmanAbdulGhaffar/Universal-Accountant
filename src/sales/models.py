from django.db import models
from inventory.models import Product, Warehouse
from partners.models import Customer
from core.models import TimeStamped

class SalesInvoice(TimeStamped):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=32, default="unpaid")

class SalesLine(models.Model):
    invoice = models.ForeignKey(SalesInvoice, related_name="lines", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=14, decimal_places=3)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    cogs = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class Payment(TimeStamped):
    invoice = models.ForeignKey(SalesInvoice, related_name="payments", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=32, default="cash")
