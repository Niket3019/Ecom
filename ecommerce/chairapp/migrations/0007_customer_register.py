# Generated by Django 4.1 on 2023-01-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairapp', '0006_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
