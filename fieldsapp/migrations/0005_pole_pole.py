# Generated by Django 2.2.8 on 2019-12-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0004_auto_20191210_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='pole',
            name='pole',
            field=models.CharField(default=1, max_length=10, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
