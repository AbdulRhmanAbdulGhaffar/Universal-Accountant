from django.db import models

class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    invoice_footer = models.TextField(blank=True)
