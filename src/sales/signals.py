from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SalesLine
from inventory.costing_services import consume_fifo

@receiver(post_save, sender=SalesLine)
def set_cogs_on_salesline(sender, instance, created, **kwargs):
    if created and instance.qty:
        total_cost, used = consume_fifo(instance.product, instance.warehouse, instance.qty)
        instance.cogs = total_cost
        instance.save(update_fields=["cogs"])
