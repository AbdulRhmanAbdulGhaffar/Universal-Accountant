from django.db import models
from core.models import TimeStamped
from inventory.models import Product, Warehouse
from partners.models import Supplier

class PurchaseInvoice(TimeStamped):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    date = models.DateField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class PurchaseLine(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice, related_name="lines", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=14, decimal_places=3)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2)
