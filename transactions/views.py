from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionView(ListCreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(RetrieveUpdateDestroyAPIView):

	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	lookup_url_kwarg = "transaction_id"