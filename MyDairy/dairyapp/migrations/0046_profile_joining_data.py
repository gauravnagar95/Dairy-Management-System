# Generated by Django 2.1.7 on 2019-03-23 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0045_customermilkcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joining_data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
