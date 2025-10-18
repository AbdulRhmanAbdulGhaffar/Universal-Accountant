from django.db import models
from core.models import TimeStamped
from .models import Product, Warehouse

class CostLayer(TimeStamped):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    qty_remaining = models.DecimalField(max_digits=14, decimal_places=3)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=4)
    ref = models.CharField(max_length=128, blank=True)

    class Meta:
        indexes = [models.Index(fields=['product','warehouse','created_at'])]
