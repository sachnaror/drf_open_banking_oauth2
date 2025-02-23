from django.urls import path
from .views import AccountBalanceView, TransferMoneyView

urlpatterns = [
    path('balance/', AccountBalanceView.as_view(), name='account-balance'),
    path('transfer/', TransferMoneyView.as_view(), name='transfer-money'),
]
