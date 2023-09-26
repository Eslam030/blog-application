from django.db import models


class users(models.Model):
    id = models.IntegerField().primary_key
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class post (models.Model):
    id = models.IntegerField().primary_key
    owner_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE
    )
    # add images
    content = models.CharField(max_length=255)
    publish_date = models.DateField()


class comment (models.Model):
    post_id = models.ForeignKey(
        post,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        users,
        on_delete=models.CASCADE
    )
    comment_content = models.CharField(max_length=255)
# Create your models here.
