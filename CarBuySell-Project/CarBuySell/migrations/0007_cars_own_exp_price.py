# Generated by Django 4.0.5 on 2022-07-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarBuySell', '0006_cars_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='own_exp_price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
