# Generated by Django 3.2.8 on 2022-02-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_alter_gameproject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameproject',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
