# Generated by Django 3.2.8 on 2022-02-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20220223_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameproject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
