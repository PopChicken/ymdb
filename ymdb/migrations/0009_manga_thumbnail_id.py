# Generated by Django 3.2.7 on 2021-09-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ymdb', '0008_alter_manga_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='thumbnail_id',
            field=models.IntegerField(default=-1),
        ),
    ]
