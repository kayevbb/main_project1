# Generated by Django 2.2.8 on 2019-12-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0005_pole_pole'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
