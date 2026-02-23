from django.db import models
from django.contrib.auth.models import User

class AbstractPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="posts/")
    text = models.TextField(max_length=1200)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.author}: {self.created_at}"

class Stories(AbstractPost):
    pass

class Post(AbstractPost):
    pass

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta: 
        unique_together = (('author', 'post'), )

    def __str__(self):
        return f"{self.author} поставил лайк посту {self.post.author} в {self.created_at}"
    
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")     
    text = models.TextField(max_length=600)
    photo = models.ImageField(upload_to="comment_media/", null=True, blank=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).all()
    
    @property
    def children_count(self):
        return Comment.objects.filter(parent=self).all().count()
    
    def __str__(self):
        return f"{self.author} оставил комментарий на посте {self.post.author}"
