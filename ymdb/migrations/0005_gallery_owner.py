# Generated by Django 3.2 on 2021-09-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ymdb', '0004_auto_20210919_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='owner',
            field=models.CharField(default='gentleman', max_length=38),
            preserve_default=False,
        ),
    ]