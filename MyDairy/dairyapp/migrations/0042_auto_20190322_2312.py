# Generated by Django 2.1.7 on 2019-03-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0041_auto_20190322_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(max_length=1000, null=True, unique=True),
        ),
    ]
