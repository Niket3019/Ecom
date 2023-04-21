# Generated by Django 4.1 on 2023-04-01 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='count_button_click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255, null=True)),
                ('tag_name', models.CharField(max_length=255, null=True)),
                ('click_count', models.CharField(max_length=255, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=20)),
                ('emailaddress', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=250)),
                ('confirmpassword', models.CharField(max_length=250)),
                ('forgot_password_token', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track_User_Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('url', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField(null=True)),
                ('region', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('date_time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VedioDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255, null=True)),
                ('start_time', models.CharField(max_length=255, null=True)),
                ('pause_time', models.CharField(max_length=255, null=True)),
                ('duration', models.CharField(max_length=255, null=True)),
                ('total_duration', models.CharField(max_length=255, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('PrevPrice', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(upload_to='upload/product/')),
                ('catergory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chairapp.catergory')),
            ],
        ),
    ]
