# Generated by Django 4.2.6 on 2023-10-30 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_answer_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tags',
        ),
    ]