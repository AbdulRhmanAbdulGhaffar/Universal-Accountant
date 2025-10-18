from rest_framework import viewsets, permissions
from .models import Product, Warehouse, Stock
from .serializers import ProductSerializer, WarehouseSerializer, StockSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["sku","name"]
    search_fields = ["sku","name"]
    ordering_fields = ["created_at","price","cost"]

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["name"]
    search_fields = ["name","location"]
    ordering_fields = ["created_at","name"]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.select_related("product","warehouse")
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["product","warehouse"]
    ordering_fields = ["quantity","updated_at"]
