# Generated by Django 3.1 on 2020-09-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200907_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]