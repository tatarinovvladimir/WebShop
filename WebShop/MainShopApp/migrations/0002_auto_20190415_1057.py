# Generated by Django 2.1.5 on 2019-04-15 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainShopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimg',
            name='img',
            field=models.ImageField(editable=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='itemimg',
            name='item',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='MainShopApp.Item'),
        ),
    ]
