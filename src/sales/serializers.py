from rest_framework import serializers
from .models import SalesInvoice, SalesLine, Payment

class SalesLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesLine
        fields = ("id","product","warehouse","qty","unit_price")

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id","invoice","amount","method","created_at")

class SalesInvoiceSerializer(serializers.ModelSerializer):
    lines = SalesLineSerializer(many=True)
    payments = PaymentSerializer(many=True, read_only=True)
    class Meta:
        model = SalesInvoice
        fields = ("id","customer","date","subtotal","discount","tax","total","status","lines","payments")

    def create(self, validated_data):
        lines = validated_data.pop("lines", [])
        inv = SalesInvoice.objects.create(**validated_data)
        for l in lines:
            SalesLine.objects.create(invoice=inv, **l)
        return inv
