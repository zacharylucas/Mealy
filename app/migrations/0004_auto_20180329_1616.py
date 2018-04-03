# Generated by Django 2.0.2 on 2018-03-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180329_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_preference',
            name='breakTime',
        ),
        migrations.RemoveField(
            model_name='user_preference',
            name='dinnerTime',
        ),
        migrations.RemoveField(
            model_name='user_preference',
            name='lunchTime',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='breakTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='dinnerTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='lunchTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
