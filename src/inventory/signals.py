from django.db.models.signals import post_save
from django.dispatch import receiver
from purchases.models import PurchaseLine
from sales.models import SalesLine
from .services import apply_stock_movement
from .models import StockMovement

@receiver(post_save, sender=PurchaseLine)
def on_purchase_line_created(sender, instance, created, **kwargs):
    if created:
        apply_stock_movement(
            instance.product, instance.warehouse, instance.qty,
            instance.unit_cost, StockMovement.IN, ref=f"PI#{instance.invoice_id}"
        )

@receiver(post_save, sender=SalesLine)
def on_sales_line_created(sender, instance, created, **kwargs):
    if created:
        apply_stock_movement(
            instance.product, instance.warehouse, instance.qty,
            instance.unit_price, StockMovement.OUT, ref=f"SI#{instance.invoice_id}"
        )
