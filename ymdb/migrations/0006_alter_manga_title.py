# Generated by Django 3.2 on 2021-09-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ymdb', '0005_gallery_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
