# Generated by Django 3.2.4 on 2021-09-20 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210915_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='is_follow',
        ),
    ]