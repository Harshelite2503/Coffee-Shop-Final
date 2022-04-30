from django.shortcuts import render
from rest_framework import generics
from .models import CustomerInfo, Bill, Outlet, OutletPhone, Waiter, WaiterOrderID, ItemDetails, Inventory, InventoryDistributor,Creates
from .serializers import CustomerInfoSerializer,BillInfoSerializer, InventoryInfoSerializer, WaiterinfoSerializer
# Create your views here.
from django.views.generic import ListView,UpdateView,DeleteView,DetailView,CreateView
from django.urls import reverse_lazy
# class CustomerList(generics.ListCreateAPIView):
#     queryset = CustomerInfo.objects.all()
#     serializer_class = CustomerInfoSerializer    

# class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomerInfo.objects.all()
#     serializer_class = CustomerInfoSerializer

class CustomerListView(ListView):
     model = CustomerInfo
     template_name = 'customer_list.html'

class CustomerDetailView(DetailView):
     model = CustomerInfo
     template_name = 'customer_detail.html'

class CustomerEditView(UpdateView):
     model = CustomerInfo
     template_name = 'customer_edit.html'
     fields = ('customerName' , 'customerPhone', 'waiterID')
     success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
     model = CustomerInfo
     template_name = 'customer_delete.html'
     success_url = reverse_lazy('customer_list')

class CustomerCreateView(CreateView):
     model = CustomerInfo
     template_name = 'customer_create.html'
     fields = ('customerName' , 'customerPhone','waiterID')
     success_url = reverse_lazy('customer_list')

######################################################################################

class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillInfoSerializer

class BillDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillInfoSerializer

#######################################################################################

class WaiterListView(ListView):
     model = Waiter
     template_name = 'waiter_list.html'

class WaiterDetailView(DetailView):
     model = Waiter
     template_name = 'waiter_detail.html'
     fields = ('firstName' , 'lastName', 'outletID')

class WaiterEditView(UpdateView):
     model = Waiter
     template_name = 'waiter_edit.html'
     fields = ('firstName' , 'lastName', 'outletID')
     success_url = reverse_lazy('waiter_list')

class WaiterDeleteView(DeleteView):
     model = Waiter
     template_name = 'waiter_delete.html'
     success_url = reverse_lazy('waiter_list')

class WaiterCreateView(CreateView):
     model = Waiter
     template_name = 'waiter_create.html'
     fields = ('firstName' , 'LastName', 'outletID')
     success_url = reverse_lazy('waiter_list')

######################################################################################

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryInfoSerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryInfoSerializer



