from django.shortcuts import render
from rest_framework import viewsets, permissions, pagination
from .models import Receipts
# Create your views here.

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipts.objects.all()
