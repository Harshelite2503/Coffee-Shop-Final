from django.urls import path
from .views import BillAddView, BillCreateView, BillDeleteView, BillDetailView, BillListView, CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerEditView,CustomerListView, DistributorCreateView, InventoryCreateView, InventoryDeleteView, InventoryDetailView, InventoryEditView, InventoryListView, ItemCreateView, ItemDeleteView, ItemDetailView, ItemEditView, ItemListView, WaiterCreateView, WaiterDeleteView, WaiterDetailView, WaiterEditView, WaiterListView

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name = 'customer_detail'),
    path('customers/', CustomerListView.as_view(),name = 'customer_list'),
    path('customers/add/' ,CustomerCreateView.as_view(), name = 'customer_create'),
    path('customers/<int:pk>/edit/' ,CustomerEditView.as_view(), name = 'customer_edit'),
    path('customers/<int:pk>/delete/' ,CustomerDeleteView.as_view(), name = 'customer_delete'),
    
    # path('bills/', BillList.as_view()),
    # path('bills/<int:pk>/', BillDetails.as_view()),
    
    path('waiter/<int:pk>/', WaiterDetailView.as_view(), name = 'waiter_detail'),
    path('waiter/', WaiterListView.as_view(),name = 'waiter_list'),
    path('waiter/add/' ,WaiterCreateView.as_view(), name = 'waiter_create'),
    path('waiter/<int:pk>/edit/' ,WaiterEditView.as_view(), name = 'waiter_edit'),
    path('waiter/<int:pk>/delete/' ,WaiterDeleteView.as_view(), name = 'waiter_delete'),
    
    path('item/<int:pk>/', ItemDetailView.as_view(), name = 'item_detail'),
    path('item/', ItemListView.as_view(),name = 'item_list'),
    path('item/add/' ,ItemCreateView.as_view(), name = 'item_create'),
    path('item/<int:pk>/edit/' ,ItemEditView.as_view(), name = 'item_edit'),
    path('item/<int:pk>/delete/' ,ItemDeleteView.as_view(), name = 'item_delete'),

    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name = 'inventory_detail'),
    path('inventory/', InventoryListView.as_view(),name = 'inventory_list'),
    path('inventory/add/' ,InventoryCreateView.as_view(), name = 'inventory_create'),
    path('inventory/<int:pk>/edit/' ,InventoryEditView.as_view(), name = 'inventory_edit'),
    path('inventory/<int:pk>/delete/' ,InventoryDeleteView.as_view(), name = 'inventory_delete'),
    
    path('bill/', BillListView.as_view(),name = 'bill_list'),
    path('bill/<int:pk>/', BillDetailView.as_view(), name = 'bill_detail'),
    path('bill/<int:pk>/delete/' ,BillDeleteView.as_view(), name = 'bill_delete'),
    path('bill/add/', BillCreateView.as_view(), name = 'bill_create'),
    path('bill/add/details/', BillAddView.as_view(), name = 'bill_add'),
    
    path('distributors/add/', DistributorCreateView.as_view(), name = 'distributor_create'),
]