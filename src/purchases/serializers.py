from rest_framework import serializers
from .models import PurchaseInvoice, PurchaseLine

class PurchaseLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLine
        fields = ("id","product","warehouse","qty","unit_cost")

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    lines = PurchaseLineSerializer(many=True)
    class Meta:
        model = PurchaseInvoice
        fields = ("id","supplier","date","subtotal","discount","tax","total","lines")

    def create(self, validated_data):
        lines = validated_data.pop("lines", [])
        inv = PurchaseInvoice.objects.create(**validated_data)
        for l in lines:
            PurchaseLine.objects.create(invoice=inv, **l)
        return inv
