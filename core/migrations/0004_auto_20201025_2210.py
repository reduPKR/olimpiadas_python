# Generated by Django 3.1 on 2020-10-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_athletegame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='age',
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
