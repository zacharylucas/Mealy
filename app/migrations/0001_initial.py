# Generated by Django 2.0.2 on 2018-04-04 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('break_lunch_dinner', models.IntegerField()),
                ('discoveryId', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('gain_lose_maintain', models.IntegerField()),
                ('cell', models.CharField(default='', max_length=12)),
                ('breakTime', models.TimeField(blank=True, null=True)),
                ('lunchTime', models.TimeField(blank=True, null=True)),
                ('dinnerTime', models.TimeField(blank=True, null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
