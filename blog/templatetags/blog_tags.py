from django import template
from blog import models

register = template.Library()

@register.simple_tag
def get_recent_post(num=5):
    return models.Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return models.Post.objects.dates('created_time', 'month', order='DESC')
    # dates 方法会返回一个列表, 列表中的元素为每一篇文章(Post)的创建时间，且是 Python 的 date 对象，精确到月份，降序排列

@register.simple_tag
def get_categories():
    return models.Category.objects.all()

