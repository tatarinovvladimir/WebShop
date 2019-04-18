# Generated by Django 2.1.5 on 2019-04-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainShopApp', '0005_auto_20190415_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='aviable',
            field=models.CharField(choices=[('В наличии', 'В наличии'), ('Нет на складе', 'Нет на складе')], default='Нет на складе', max_length=50),
        ),
        migrations.AlterField(
            model_name='itemimg',
            name='item',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='img', to='MainShopApp.Item'),
        ),
    ]
