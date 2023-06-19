# Generated by Django 4.2.2 on 2023-06-19 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_availability_remove_room_end_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name': 'Availability', 'verbose_name_plural': 'Availabilities'},
        ),
        migrations.RemoveField(
            model_name='room',
            name='availability',
        ),
        migrations.AddField(
            model_name='availability',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
            preserve_default=False,
        ),
    ]
