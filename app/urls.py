from django.urls import path
from .views import CustomerList, CustomerDetail, BillList #BillDetail

urlpatterns = [
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    path('customers/', CustomerList.as_view()),
    path('bills/', BillList.as_view()),
    #path('bills/<int:pk>/', BillDetail.as_view()),
]