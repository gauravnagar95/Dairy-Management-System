# Generated by Django 2.1.7 on 2019-03-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0030_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]
