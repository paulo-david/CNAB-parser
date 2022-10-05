# Generated by Django 4.1.2 on 2022-10-05 18:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=19)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='users.user')),
            ],
        ),
    ]
