# Generated by Django 3.1 on 2024-03-20 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20240320_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageunits',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]