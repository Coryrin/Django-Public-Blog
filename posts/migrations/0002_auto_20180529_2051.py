# Generated by Django 2.0.4 on 2018-05-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message_html',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='hello', unique=True),
            preserve_default=False,
        ),
    ]