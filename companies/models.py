from uuid import uuid4
from django.db.models import Model, UUIDField, CharField, ForeignKey, CASCADE


class Company(Model):
    id = UUIDField(default=uuid4, unique=True,
                   primary_key=True, editable=False)
    name = CharField(max_length=19)

    owner = ForeignKey("users.User", on_delete=CASCADE,
                       related_name="companies")
