# Generated by Django 3.2.8 on 2021-10-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
