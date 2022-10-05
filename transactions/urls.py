from django.urls import path

from transactions.views import TransactionView, TransactionDetailView

urlpatterns = [
    path("transactions/", TransactionView.as_view()),
    path("transactions/<uuid:transaction_id>/", TransactionDetailView.as_view()),
]
