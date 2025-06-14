# Generated by Django 5.0.1 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0011_room_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.CharField(choices=[('AC', 'AC'), ('NON-AC', 'NON-AC'), ('QUEEN', 'QUEEN'), ('DELUX', 'DELUX'), ('KING', 'KING')], max_length=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=50),
        ),
    ]
