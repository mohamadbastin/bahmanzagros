# Generated by Django 2.1.7 on 2019-05-23 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0038_auto_20190523_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tour_registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='tour.TourRegistration'),
        ),
    ]
