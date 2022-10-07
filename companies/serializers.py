from rest_framework.serializers import ModelSerializer, SerializerMethodField
from companies.models import Company
from transactions.models import TransactionTypes


class CompanySerializer(ModelSerializer):

    balance = SerializerMethodField()

    def get_balance(self, obj):

        counter = 0

        for transaction in obj.transactions.all():

            typeIdx = int(transaction.type) - 1
            transactionValue = int(transaction.value)

            if TransactionTypes[typeIdx][1][-1] == "+":
                counter = counter + transactionValue
            else:
                counter = counter - transactionValue

        return counter/100

    class Meta:
        model = Company
        fields = "__all__"
