# Generated by Django 4.1 on 2022-10-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/product/'),
        ),
    ]