# Generated by Django 2.1.5 on 2019-04-15 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainShopApp', '0003_auto_20190415_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimg',
            name='img',
            field=models.ImageField(upload_to='WebShopApp/media'),
        ),
        migrations.AlterField(
            model_name='itemimg',
            name='item',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='MainShopApp.Item'),
        ),
    ]
