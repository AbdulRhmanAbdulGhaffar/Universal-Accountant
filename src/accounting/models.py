from django.db import models
from core.models import TimeStamped

class Account(TimeStamped):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=32)  # asset, liability, revenue, expense, equity

class JournalEntry(TimeStamped):
    date = models.DateField()
    memo = models.CharField(max_length=255, blank=True)

class LedgerEntry(models.Model):
    journal = models.ForeignKey(JournalEntry, related_name="entries", on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=14, decimal_places=2, default=0)
