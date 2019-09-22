from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 博客类型
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
# 博客
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<blog:%s>".format(self.title)