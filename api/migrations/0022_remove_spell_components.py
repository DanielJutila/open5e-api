# Generated by Django 3.2.18 on 2023-04-15 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20230415_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='components',
        ),
    ]