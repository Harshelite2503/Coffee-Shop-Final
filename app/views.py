from django.shortcuts import render
from rest_framework import generics
from .models import CustomerInfo, Bill, Outlet, OutletPhone, Waiter, WaiterOrderID, ItemDetails, Inventory, InventoryDistributor,Creates
from .serializers import CustomerInfoSerializer,BillInfoSerializer
# Create your views here.

class CustomerList(generics.ListAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerInfoSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerInfoSerializer

class BillList(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillInfoSerializer
