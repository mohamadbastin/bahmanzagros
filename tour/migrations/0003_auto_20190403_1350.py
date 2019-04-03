# Generated by Django 2.0.9 on 2019-04-03 13:50

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_tourregistration_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='city',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='national_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='nationality',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
