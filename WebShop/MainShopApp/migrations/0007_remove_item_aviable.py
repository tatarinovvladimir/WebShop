# Generated by Django 2.1.5 on 2019-04-15 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainShopApp', '0006_auto_20190415_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='aviable',
        ),
    ]