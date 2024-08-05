# Generated by Django 3.2.20 on 2024-07-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.CharField(editable=False, max_length=255, unique=True)),
                ('amount', models.IntegerField()),
                ('payment_data', models.JSONField()),
                ('charge_created', models.DateTimeField()),
                ('fetched', models.DateTimeField()),
            ],
        ),
    ]
