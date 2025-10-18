from rest_framework import viewsets, permissions
from .models import Account, JournalEntry
from .serializers import AccountSerializer, JournalEntrySerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["type"]
    ordering_fields = ["code","name"]

class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["date"]
    ordering_fields = ["date","created_at"]
