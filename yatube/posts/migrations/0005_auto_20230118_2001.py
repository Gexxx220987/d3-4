# Generated by Django 2.2.9 on 2023-01-18 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230118_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]