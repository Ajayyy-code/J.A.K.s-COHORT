# Generated by Django 3.2.9 on 2021-11-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICC_Tracking', '0006_auto_20211125_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='bearer',
            name='bearerStatus',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Delivered')], default=1),
        ),
    ]