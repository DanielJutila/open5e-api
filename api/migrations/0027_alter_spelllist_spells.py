# Generated by Django 3.2.18 on 2023-05-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20230511_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spelllist',
            name='spells',
            field=models.ManyToManyField(help_text='The set of spells.', related_name='spell_lists', to='api.Spell'),
        ),
    ]