from django.db import models
from core.models import TimeStamped

class PartnerBase(TimeStamped):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    class Meta:
        abstract = True

class Customer(PartnerBase):
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class Supplier(PartnerBase):
    pass

class Interaction(TimeStamped):
    partner_type = models.CharField(max_length=10, choices=[("customer","Customer"),("supplier","Supplier")])
    partner_id = models.PositiveIntegerField()
    note = models.TextField()
