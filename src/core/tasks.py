from celery import shared_task
from django.core.mail import send_mail
from django.db.models import F
from inventory.models import Stock

@shared_task
def check_low_stock_and_notify():
    lows = Stock.objects.filter(quantity__lt=F('product__min_stock')).select_related('product')
    if lows.exists():
        body = "\n".join([f"{s.product.name}: {s.quantity}" for s in lows])
        send_mail("تنبيه انخفاض المخزون", body, "noreply@ua.local", ["admin@ua.local"])
