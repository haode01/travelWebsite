# Generated by Django 2.1.2 on 2018-10-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_myuser_integral'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='check_time',
            field=models.DateField(default='1970-01-01', verbose_name='签到时间'),
        ),
    ]