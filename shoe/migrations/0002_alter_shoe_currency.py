# Generated by Django 4.1.3 on 2022-11-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='currency',
            field=models.CharField(choices=[('€', 'EURO (€)')], default='€', max_length=5),
        ),
    ]
