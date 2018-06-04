from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True, null= True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True,null=True)

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    # 自定义 get_absolute_url 方法, 为了方便地生成URL
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
        # return reverse('blog:detail', kwargs={'pk': self.pk})
        # 'blog:detail'，意思是 blog 应用下的 name=detail 的函数

    class Meta:
        ordering = ['-created_time','title']

