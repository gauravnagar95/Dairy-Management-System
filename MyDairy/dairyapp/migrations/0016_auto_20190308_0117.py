# Generated by Django 2.1.7 on 2019-03-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0015_auto_20190307_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorledger',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Sunday', max_length=2),
        ),
    ]
