from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200, default="test")
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="posts/")
    text = models.TextField(max_length=1200)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.author}: {self.created_at}"
