from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def kpis(request):
    return Response({
        "today_sales_total": 0,
        "today_purchases_total": 0,
        "month_profit": 0,
        "low_stock_count": 0,
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def sales_series(request):
    labels = ["1","2","3","4","5","6","7"]
    values = [1200,900,1500,800,1600,1400,1700]
    return Response({"labels": labels, "values": values})
