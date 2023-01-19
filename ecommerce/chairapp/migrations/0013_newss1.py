# Generated by Django 4.1 on 2023-01-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairapp', '0012_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newss1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]