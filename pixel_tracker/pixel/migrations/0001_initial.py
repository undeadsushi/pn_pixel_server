# Generated by Django 2.1.1 on 2018-09-27 22:02

from django.db import migrations, models
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PixelEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurred_at', django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True)),
                ('member_id', models.IntegerField()),
                ('action', models.CharField(choices=[('v', 'VIEW'), ('c', 'CONVERT')], max_length=200)),
                ('pn_cookie_id', models.CharField(max_length=200)),
                ('ip_address', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('referring_url', models.CharField(max_length=200)),
                ('user_agent', models.CharField(max_length=200)),
            ],
        ),
    ]
