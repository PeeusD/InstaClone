# Generated by Django 3.2.4 on 2021-09-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_follow_is_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='followed',
        ),
    ]