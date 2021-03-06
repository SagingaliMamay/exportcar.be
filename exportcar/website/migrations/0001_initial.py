# Generated by Django 4.0.3 on 2022-03-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=15)),
                ('year', models.IntegerField(max_length=10)),
                ('nrg', models.CharField(max_length=15)),
                ('transmission', models.CharField(max_length=15)),
                ('km', models.IntegerField(max_length=10)),
                ('price', models.IntegerField(max_length=6)),
                ('description', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
