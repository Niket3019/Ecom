# Generated by Django 4.1 on 2022-11-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairapp', '0005_product_prevprice_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
