from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.ui_views import products_page, customers_page
from sales.views import SalesInvoiceViewSet, PaymentViewSet, print_invoice
from purchases.views import PurchaseInvoiceViewSet
from inventory.views import ProductViewSet, WarehouseViewSet, StockViewSet
from partners.views import CustomerViewSet, SupplierViewSet
from accounting.views import AccountViewSet, JournalEntryViewSet
from dashboard.api import kpis, sales_series

router = routers.DefaultRouter()
router.register(r"sales/invoices", SalesInvoiceViewSet, basename="sales-invoices")
router.register(r"sales/payments", PaymentViewSet, basename="sales-payments")
router.register(r"purchases/invoices", PurchaseInvoiceViewSet, basename="purchases-invoices")
router.register(r"inventory/products", ProductViewSet, basename="inventory-products")
router.register(r"inventory/warehouses", WarehouseViewSet, basename="inventory-warehouses")
router.register(r"inventory/stocks", StockViewSet, basename="inventory-stocks")
router.register(r"partners/customers", CustomerViewSet, basename="partners-customers")
router.register(r"partners/suppliers", SupplierViewSet, basename="partners-suppliers")
router.register(r"accounting/accounts", AccountViewSet, basename="accounting-accounts")
router.register(r"accounting/journals", JournalEntryViewSet, basename="accounting-journals")

urlpatterns = [
    path("ui/products/", products_page, name="ui-products"),
    path("ui/customers/", customers_page, name="ui-customers"),
    path("sales/invoices/<int:pk>/print/", print_invoice, name="print-invoice"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/", include("users.urls")),
    path("", include("dashboard.urls")),
    path("api/dashboard/kpis", kpis),
    path("api/dashboard/sales-series", sales_series),
]
