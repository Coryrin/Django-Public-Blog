# Generated by Django 2.0.4 on 2018-05-31 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20180531_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='road.jpeg', upload_to='media'),
        ),
    ]