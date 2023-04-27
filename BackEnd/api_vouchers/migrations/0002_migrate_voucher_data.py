# Generated by Django 3.2.8 on 2022-07-15 15:42
import json
import os
import uuid

from django.db import migrations

from api_accounts.constants import RoleData


def initial_data(apps, schema_editor):
    voucher_model = apps.get_model("api_vouchers", 'Voucher')
    json_data = json.load(
        open('api_vouchers/constants/voucher.json', encoding="utf8"))

    vouchers = []

    for voucher_data in json_data:
        voucher = voucher_model(id=uuid.uuid4(),
                                name=voucher_data['name'],
                                rate=voucher_data['rate'])
        vouchers.append(voucher)
    voucher_model.objects.bulk_create(vouchers)


class Migration(migrations.Migration):
    dependencies = [
        ('api_vouchers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data, migrations.RunPython.noop)
    ]
