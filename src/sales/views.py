from rest_framework import viewsets, permissions
from .models import SalesInvoice, Payment
from .serializers import SalesInvoiceSerializer, PaymentSerializer

class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all().select_related("customer")
    serializer_class = SalesInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["customer","date","status"]
    search_fields = ["customer__name"]
    ordering_fields = ["date","total"]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related("invoice")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["invoice"]
    ordering_fields = ["created_at","amount"]

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa.CreatePDF(html, dest=response, encoding='utf-8')
    return response

def print_invoice(request, pk):
    from .models import SalesInvoice
    inv = get_object_or_404(SalesInvoice.objects.select_related('customer'), pk=pk)
    return render_to_pdf('sales/invoice_pdf.html', { 'invoice': inv, 'lines': inv.lines.select_related('product','warehouse') })
