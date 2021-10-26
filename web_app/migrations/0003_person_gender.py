# Generated by Django 3.2.8 on 2021-10-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_person_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('FE', 'Female'), ('MA', 'Male')], default='MA', max_length=2),
        ),
    ]