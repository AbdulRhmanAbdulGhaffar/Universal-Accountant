from rest_framework import viewsets, permissions
from .models import Customer, Supplier
from .serializers import CustomerSerializer, SupplierSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["name"]
    search_fields = ["name","phone","email"]
    ordering_fields = ["name","created_at"]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["name"]
    search_fields = ["name","phone","email"]
    ordering_fields = ["name","created_at"]
