# Generated by Django 3.2.16 on 2024-10-24 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Post',
        ),
    ]