from django.db import models
from core.models import TimeStamped

class Warehouse(TimeStamped):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255, blank=True)
    def __str__(self): return self.name

class Product(TimeStamped):
    sku = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=32, default="unit")
    min_stock = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    def __str__(self): return f"{self.sku} - {self.name}"

class Stock(TimeStamped):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=14, decimal_places=3, default=0)
    class Meta:
        unique_together = ("product", "warehouse")

class StockMovement(TimeStamped):
    IN = "IN"; OUT = "OUT"
    MOV_TYPES = [(IN, "In"), (OUT, "Out")]
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    qty = models.DecimalField(max_digits=14, decimal_places=3)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    movement_type = models.CharField(max_length=3, choices=MOV_TYPES)
    ref = models.CharField(max_length=128, blank=True)
