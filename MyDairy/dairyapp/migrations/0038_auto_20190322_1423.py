# Generated by Django 2.1.7 on 2019-03-22 08:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dairyapp', '0037_auto_20190322_1413'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Profile',
        ),
    ]
