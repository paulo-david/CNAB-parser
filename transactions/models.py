from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.db.models import Model, UUIDField, TextChoices, CharField, DateTimeField,  ForeignKey, CASCADE


TransactionTypes = [
    ('1', 'Débito+'),
    ('2', 'Boleto-'),
    ('3', 'Financiamento-'),
    ('4', 'Crédito+'),
    ('5', 'Recebimento Empréstimo+'),
    ('6', 'Vendas+'),
    ('7', 'Recebimento TED+'),
    ('8', 'Recebimento DOC+'),
    ('9', 'Aluguel-'),
]


class Transaction(Model):
    id = UUIDField(default=uuid4, unique=True,
                   primary_key=True, editable=False)

    type = CharField(max_length=1, choices=TransactionTypes)
    value = CharField(max_length=10)
    CPF = CharField(max_length=11)
    card = CharField(max_length=12)
    time = DateTimeField()

    company = ForeignKey("companies.Company", on_delete=CASCADE,
                         related_name="transactions")
