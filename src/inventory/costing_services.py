from decimal import Decimal
from django.db import transaction
from .costing_models import CostLayer

@transaction.atomic
def add_layer(product, warehouse, qty, unit_cost, ref=""):
    return CostLayer.objects.create(product=product, warehouse=warehouse, qty_remaining=qty, unit_cost=unit_cost, ref=ref)

@transaction.atomic
def consume_fifo(product, warehouse, qty_needed):
    """Consume cost layers FIFO; return (total_cost, layers_used list[(layer, qty_consumed, unit_cost)])."""
    remaining = Decimal(qty_needed)
    total_cost = Decimal('0')
    used = []
    layers = CostLayer.objects.select_for_update().filter(product=product, warehouse=warehouse, qty_remaining__gt=0).order_by('created_at','id')
    for layer in layers:
        if remaining <= 0:
            break
        take = min(layer.qty_remaining, remaining)
        if take > 0:
            layer.qty_remaining = layer.qty_remaining - take
            layer.save()
            total_cost += take * layer.unit_cost
            used.append((layer, take, layer.unit_cost))
            remaining -= take
    if remaining > 0:
        # fallback: negative layer at current avg cost 0 (could be improved)
        used.append((None, remaining, Decimal('0')))
        total_cost += Decimal('0')
        remaining = Decimal('0')
    return total_cost, used
