from rest_framework import viewsets, permissions
from .models import PurchaseInvoice
from .serializers import PurchaseInvoiceSerializer

class PurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all().select_related("supplier")
    serializer_class = PurchaseInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["supplier","date"]
    ordering_fields = ["date","total"]
