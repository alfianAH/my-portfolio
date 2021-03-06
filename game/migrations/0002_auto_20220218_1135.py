# Generated by Django 3.2.8 on 2022-02-18 03:35

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, validators=[home.validators.validate_url])),
            ],
        ),
        migrations.CreateModel(
            name='GameProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('play_url', models.CharField(max_length=200, validators=[home.validators.validate_url])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gamedetail',
            name='created',
        ),
        migrations.RemoveField(
            model_name='gamedetail',
            name='play_url',
        ),
        migrations.RemoveField(
            model_name='gamedetail',
            name='updated',
        ),
    ]
