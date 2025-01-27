# Generated by Django 3.1 on 2024-03-20 01:23

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20240320_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageunits',
            name='store',
            field=models.OneToOneField(default=store.models.Store.get_default_pk, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]
