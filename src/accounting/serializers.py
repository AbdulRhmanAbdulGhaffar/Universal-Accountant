from rest_framework import serializers
from .models import Account, JournalEntry, LedgerEntry

class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerEntry
        fields = ("id","account","debit","credit")

class JournalEntrySerializer(serializers.ModelSerializer):
    entries = LedgerEntrySerializer(many=True)
    class Meta:
        model = JournalEntry
        fields = ("id","date","memo","entries")

    def create(self, validated_data):
        entries = validated_data.pop("entries", [])
        j = JournalEntry.objects.create(**validated_data)
        for e in entries:
            LedgerEntry.objects.create(journal=j, **e)
        return j

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
