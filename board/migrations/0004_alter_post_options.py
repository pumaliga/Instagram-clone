# Generated by Django 3.2.8 on 2021-10-27 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_post_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
