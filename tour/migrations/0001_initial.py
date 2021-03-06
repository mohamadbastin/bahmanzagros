# Generated by Django 2.0.9 on 2019-04-01 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20190318_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('passport_number', models.BigIntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TourGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TourRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.BooleanField()),
                ('is_local', models.BooleanField()),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tour_registrations', to='tour.Tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tour.TourGroup'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='tour_registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_tour', to='tour.TourRegistration'),
        ),
    ]
