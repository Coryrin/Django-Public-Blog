# Generated by Django 2.0.4 on 2018-05-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.gif', upload_to=''),
        ),
    ]