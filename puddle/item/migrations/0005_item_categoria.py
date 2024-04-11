# Generated by Django 5.0.3 on 2024-03-29 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_created_at_item_criado_em_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.categoria'),
        ),
    ]