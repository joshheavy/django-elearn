from django.db import models
from django.shortcuts import reverse
from courses.models import Course
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"id": self.id})

    def get_comments(self):
        return self.comments.all()


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user.username
    