# Generated by Django 4.1.3 on 2022-11-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_orderline_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_costs',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]