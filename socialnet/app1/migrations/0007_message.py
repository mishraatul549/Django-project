# Generated by Django 2.1.7 on 2019-08-20 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20190806_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('commenttext', models.CharField(max_length=100)),
                ('messagetext', models.CharField(max_length=100)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagereciever', to='app1.signup')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagesender', to='app1.signup')),
            ],
        ),
    ]