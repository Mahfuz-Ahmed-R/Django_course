from django.urls import path, include
from . import views


urlpatterns = [
    path('deposit/', views.DepositMoneyView.as_view(), name='deposit_money'),
    path('transaction/', views.TransactionReportView.as_view(), name='transaction_report'),
    path('withdraw/', views.WithdrawMoneyView.as_view(), name='withdraw_money'),
    path('loan_request/', views.LoanMoneyView.as_view(), name='loan_request'),
    path('loans/', views.LoanList.as_view(), name='loan_list'),
    path('loan/<int:loan_id>/', views.PayLoanView.as_view(), name='deposit_money'),
]
