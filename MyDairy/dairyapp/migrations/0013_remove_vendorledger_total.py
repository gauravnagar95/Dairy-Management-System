# Generated by Django 2.1.7 on 2019-03-05 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0012_vendorledger_related_milkcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorledger',
            name='total',
        ),
    ]
