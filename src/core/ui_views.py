from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from inventory.models import Product
from partners.models import Customer

@require_GET
def products_page(request):
    return render(request, "inventory/products_list.html", {"products": Product.objects.all()})

@require_GET
def customers_page(request):
    return render(request, "partners/customers_list.html", {"customers": Customer.objects.all()})
