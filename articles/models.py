from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import Users


class Article(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Users, related_name="like_articles")
    bookmarks = models.ManyToManyField(Users, related_name="bookmark_articles")

    def __str__(self):
        return str(self.title)



class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

