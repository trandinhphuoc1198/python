# Generated by Django 3.2.8 on 2022-04-15 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_room_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.topic'),
        ),
    ]
