# Generated by Django 4.1.3 on 2022-11-04 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderline',
            old_name='Shoe',
            new_name='shoe',
        ),
    ]