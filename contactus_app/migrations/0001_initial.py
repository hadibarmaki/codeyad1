# Generated by Django 4.2.14 on 2024-10-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=50)),
            ],
        ),
    ]
