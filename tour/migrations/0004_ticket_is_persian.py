# Generated by Django 2.1.7 on 2019-04-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20190401_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_persian',
            field=models.BooleanField(default=True),
        ),
    ]