# Generated by Django 2.0.9 on 2019-03-19 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='visible',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tour_registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_tour', to='tour.TourRegistration'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tour.TourGroup'),
        ),
        migrations.AlterField(
            model_name='tourregistration',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tour_registrations', to='tour.Tour'),
        ),
    ]
