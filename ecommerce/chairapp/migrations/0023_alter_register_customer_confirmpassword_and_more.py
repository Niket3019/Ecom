# Generated by Django 4.1 on 2023-01-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairapp', '0022_alter_register_customer_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_customer',
            name='confirmpassword',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='register_customer',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
