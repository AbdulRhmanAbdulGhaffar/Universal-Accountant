from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseLine
from inventory.costing_services import add_layer

@receiver(post_save, sender=PurchaseLine)
def create_cost_layer_on_purchase(sender, instance, created, **kwargs):
    if created:
        add_layer(instance.product, instance.warehouse, instance.qty, instance.unit_cost, ref=f"PI#{instance.invoice_id}")
