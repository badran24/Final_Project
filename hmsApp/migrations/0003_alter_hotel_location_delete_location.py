# Generated by Django 5.0.1 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
