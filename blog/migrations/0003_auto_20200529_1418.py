# Generated by Django 3.0.6 on 2020-05-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='postpics'),
        ),
    ]
