# Generated by Django 4.2.5 on 2023-09-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0011_rename_post_id_comment_post_and_more'),
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
            name='Post',
        ),
    ]
