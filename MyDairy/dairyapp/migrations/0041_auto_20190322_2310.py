# Generated by Django 2.1.7 on 2019-03-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0040_auto_20190322_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(max_length=1000, null=True),
        ),
    ]
