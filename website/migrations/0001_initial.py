# Generated by Django 4.0.3 on 2022-05-26 23:01

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
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('nrg', models.CharField(max_length=15)),
                ('transmission', models.CharField(max_length=15)),
                ('km', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=800)),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
