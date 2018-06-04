from django import template
from blog import models
from django.db.models.aggregates import Count

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
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    # 除了返回数据库中全部 Category 的记录, 还会计算Post的行数并保存在num_posts
    # 使用 filter 方法把 num_posts 的值小于 0 的分类过滤掉
    return models.Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gte=0)

