# Generated by Django 4.0.5 on 2022-06-14 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarBuySell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='firstname',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='lastname',
            new_name='password',
        ),
    ]
