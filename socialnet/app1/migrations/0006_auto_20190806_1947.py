# Generated by Django 2.1.7 on 2019-08-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20190427_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendslist',
            unique_together={('sender', 'reciever')},
        ),
    ]
