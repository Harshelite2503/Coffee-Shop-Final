from django.urls import path
from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerEditView, BillList,BillDetails, CustomerListView,WaiterList, WaiterDetail,InventoryList, InventoryDetail

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name = 'customer_detail'),
    path('customers/', CustomerListView.as_view(),name = 'customer_list'),
    path('customers/add/' ,CustomerCreateView.as_view(), name = 'customer_create'),
    path('customers/<int:pk>/edit/' ,CustomerEditView.as_view(), name = 'customer_edit'),
    path('customers/<int:pk>/delete/' ,CustomerDeleteView.as_view(), name = 'customer_delete'),
    path('bills/', BillList.as_view()),
    path('bills/<int:pk>/', BillDetails.as_view()),
    path('waiter/', WaiterList.as_view()),
    path('waiter/<int:pk>/', WaiterDetail.as_view()),
    path('inventory/', InventoryList.as_view() ),
    path('inventory/<int:pk>', InventoryDetail.as_view()),
    
]