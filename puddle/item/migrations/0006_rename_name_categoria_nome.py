# Generated by Django 5.0.3 on 2024-03-30 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_item_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='nome',
        ),
    ]
