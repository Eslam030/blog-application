from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Post (models.Model):
    title = models.CharField(max_length=255)
    statue = models.CharField(max_length=2)
    content = HTMLField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class comment (models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment_content = models.CharField(max_length=255)
    publish_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content


# Create your models here.
