# Generated by Django 3.2.8 on 2021-10-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='static/avatar.png', upload_to='avatars/'),
        ),
    ]
