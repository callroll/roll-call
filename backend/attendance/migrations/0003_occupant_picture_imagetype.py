# Generated by Django 4.1.7 on 2023-03-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_occupant_deleted_at_room_x_occupant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant_picture',
            name='imageType',
            field=models.CharField(blank=True, default='profile', max_length=10),
        ),
    ]
