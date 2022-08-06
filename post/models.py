from distutils.command.upload import upload
from django.db import models

class Tag(models.Model):
    tag_content = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True, null=True, upload_to = "Files")
    tagging = models.ManyToManyField(Tag, related_name='tagged')

    def __str__(self):
        return self.title

