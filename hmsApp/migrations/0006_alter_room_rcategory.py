# Generated by Django 5.0.1 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0005_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='rcategory',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('DEL', 'DELUX'), ('QUE', 'QUEEN'), ('KIN', 'KING'), ('AC', 'AC')], max_length=3),
        ),
    ]
