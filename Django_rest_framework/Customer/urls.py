from django.urls import path
from Customer.views import(
    CustomerDetail,
    CustomerList,
)

urlpatterns = [
path('Create', CustomerList.as_view()),
path('detail/<int:pk>', CustomerDetail.as_view())
]


