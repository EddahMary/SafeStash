# Generated by Django 3.1 on 2024-03-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20240324_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='specifications',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
