# Generated by Django 5.0.1 

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('2 Star', '2 Star'), ('3 Star', '3 Star'), ('4 Star', '4 Star'), ('5 Star', '5 Star')], max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='hotel_pics')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmsApp.location')),
            ],
        ),
    ]
