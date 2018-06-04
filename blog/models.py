from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
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

    views = models.PositiveIntegerField(default=0)  # 记录阅读量
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

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个Markdown类, 用于渲染body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)
