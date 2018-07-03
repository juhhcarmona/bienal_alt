# Generated by Django 2.0.6 on 2018-07-03 11:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_populate_questons_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='action',
            name='questions',
            field=models.ManyToManyField(related_name='actions', to='actions.QuestionTag', verbose_name='Perguntas'),
        ),
    ]
