# Generated by Django 3.2.8 on 2021-10-23 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_alter_coordinate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]