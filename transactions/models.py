from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.db.models import Model, UUIDField, TextChoices, CharField, DateTimeField,  ForeignKey, CASCADE


class Transaction(Model):
    id = UUIDField(default=uuid4, unique=True,
                   primary_key=True, editable=False)

    class TransactionTypes(TextChoices):
        DEBITO = '1', _('Débito+')
        BOLETO = '2', _('Boleto-')
        FINANCIAMENTO = '3', _('Financiamento-')
        CREDITO = '4', _('Crédito+')
        RECEBIMENTO_EMPRESTIMO = '5', _('Recebimento Empréstimo+')
        VENDAS = '6', _('Vendas+')
        RECEBIMENTO_TED = '7', _('Recebimento TED+')
        RECEBIMENTO_DOC = '8', _('Recebimento DOC+')
        ALUGUEL = '9', _('Aluguel-')

    type = CharField(max_length=1, choices=TransactionTypes.choices)
    value = CharField(max_length=10)
    CPF = CharField(max_length=11)
    card = CharField(max_length=12)
    time = DateTimeField()

    company = ForeignKey("companies.Company", on_delete=CASCADE,
                         related_name="transactions")
