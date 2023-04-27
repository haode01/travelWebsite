# Generated by Django 2.1.2 on 2018-11-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_shoppingcart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='is_check',
            field=models.BooleanField(default=False, verbose_name='是否选中'),
        ),
    ]