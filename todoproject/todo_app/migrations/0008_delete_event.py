# Generated by Django 5.1.1 on 2024-10-30 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]