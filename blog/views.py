from django.shortcuts import render, get_object_or_404
from blog import models
# Create your views here.
import markdown
from comments.forms import CommentForm


def index(request):
    post_list = models.Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    # 导入的 get_object_or_404 方法，其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在
    # print(post,'!!!!!!!')

    # 阅读量 +1
    post.increase_views()

    # 把 Markdown 文本转为 HTML 文本再传递给模板
    # pip install markdown | pip install pygments
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    # https://www.jianshu.com/p/1e402922ee32/
    # https://www.appinn.com/markdown/
    form  = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post, 'form':form, 'comment_list':comment_list}

    return render(request, 'blog/detail.html', context=context)

def arhchives(request, year, month):
    post_list = models.Post.objects.filter(created_time__year=year,
                                           created_time__month=month,
                                           )
    return render(request,'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(models.Category, pk=pk)
    post_list = models.Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list': post_list})



