# Generated by Django 4.1.7 on 2023-02-23 21:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('name', models.CharField(max_length=100)),
                ('prefs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Occupant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('name', models.CharField(max_length=100)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.facility')),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='installation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.installation'),
        ),
    ]
