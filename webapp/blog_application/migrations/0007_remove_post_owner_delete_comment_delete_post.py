# Generated by Django 4.2.5 on 2023-09-26 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
