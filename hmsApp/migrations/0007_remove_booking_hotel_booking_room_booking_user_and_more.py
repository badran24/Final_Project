# Generated by Django 5.0.1 

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsApp', '0006_alter_room_rcategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='hmsApp.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='rcategory',
            field=models.CharField(choices=[('NAC', 'NON-AC'), ('KIN', 'KING'), ('QUE', 'QUEEN'), ('DEL', 'DELUX'), ('AC', 'AC')], max_length=3),
        ),
    ]
