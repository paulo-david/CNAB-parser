from uuid import uuid4
from django.db.models import Model, UUIDField, CharField


class User(Model):
    id = UUIDField(default=uuid4, unique=True,
                   primary_key=True, editable=False)
    name = CharField(max_length=14)
