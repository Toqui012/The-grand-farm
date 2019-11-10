# Generated by Django 2.2.7 on 2019-11-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0004_auto_20191110_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_food',
            name='pay',
            field=models.CharField(choices=[('Tarjeta', 'Tarjeta'), ('Paypal', 'Paypal')], default='Tarjeta', max_length=255),
        ),
        migrations.AlterField(
            model_name='payment_food',
            name='product',
            field=models.CharField(choices=[('Dapac Cerdas', 'Dapac Cerdas'), ('Aviplus', 'Aviplus'), ('Camperbroiler Granulado', 'Camperbroiler Granulado'), ('Conchilla', 'Conchilla'), ('Dapac Vacas', 'Dapac Vacas'), ('Nantacor', 'Nantacor'), ('Guidolin Nutri Potros', 'Guidolin Nutri Potros'), ('Red Kite', 'Red Kite')], default='Dapac Cerdas', max_length=255),
        ),
    ]