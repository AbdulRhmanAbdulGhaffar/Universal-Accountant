from django.db import transaction
from .models import Stock, StockMovement

@transaction.atomic
def apply_stock_movement(product, warehouse, qty, unit_cost, movement_type, ref=""):
    sm = StockMovement.objects.create(
        product=product, warehouse=warehouse, qty=qty,
        unit_cost=unit_cost, movement_type=movement_type, ref=ref
    )
    stock, _ = Stock.objects.select_for_update().get_or_create(product=product, warehouse=warehouse)
    if movement_type == StockMovement.IN:
        stock.quantity = stock.quantity + qty
    else:
        stock.quantity = stock.quantity - qty
    stock.save()
    return sm
