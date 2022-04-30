from django.urls import path
from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerEditView, BillList,BillDetails, CustomerListView, WaiterCreateView, WaiterDeleteView, WaiterDetailView, WaiterEditView, InventoryList, InventoryDetail, WaiterListView

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name = 'customer_detail'),
    path('customers/', CustomerListView.as_view(),name = 'customer_list'),
    path('customers/add/' ,CustomerCreateView.as_view(), name = 'customer_create'),
    path('customers/<int:pk>/edit/' ,CustomerEditView.as_view(), name = 'customer_edit'),
    path('customers/<int:pk>/delete/' ,CustomerDeleteView.as_view(), name = 'customer_delete'),
    path('bills/', BillList.as_view()),
    path('bills/<int:pk>/', BillDetails.as_view()),
    path('waiter/<int:pk>/', WaiterDetailView.as_view(), name = 'waiter_detail'),
    path('waiter/', WaiterListView.as_view(),name = 'waiter_list'),
    path('waiter/add/' ,WaiterCreateView.as_view(), name = 'waiter_create'),
    path('waiter/<int:pk>/edit/' ,WaiterEditView.as_view(), name = 'waiter_edit'),
    path('waiter/<int:pk>/delete/' ,WaiterDeleteView.as_view(), name = 'waiter_delete'),
    
    path('inventory/', InventoryList.as_view() ),
    path('inventory/<int:pk>', InventoryDetail.as_view()),
    
]