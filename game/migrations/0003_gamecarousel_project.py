# Generated by Django 3.2.8 on 2022-02-18 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20220218_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecarousel',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.gameproject'),
            preserve_default=False,
        ),
    ]
