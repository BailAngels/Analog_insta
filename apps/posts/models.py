from django.db import models

from apps.tags.models import Tag


class Post(models.Model):
    """ Модель поста"""
    description = models.TextField(
        max_length=300,
    )
    location = models.CharField(
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts",
    )

    def __str__(self):
        return f"{self.description}"


class Images(models.Model):
    image = models.ImageField(
        upload_to="images/",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="images",
    )
