from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from blog import models

from comments import models
from .forms import CommentForm
from django.views.generic import ListView
# Create your views here.



def post_comment(request, post_pk):
    print(123213)
    # 先获取被评论的文章, 后面需要把评论和被评论的文章关联起来
    # get_object_or_404这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户
    post = get_object_or_404(models.Post, pk=post_pk)
    print(post)

    if request.method == 'POST':
        form = CommentForm(request.POST)  # 生成form表单
        print('form...')

        if form.is_valid():
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)
            comment.post = post  # 将评论和被评论的文章关联起来
            comment.save()   # 将评论数据保存进数据库, 调用模型实例的 save 方法
            print('bao cun cheng gong')

            # 重定向到 post 的详情页, 实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，然后重定向到 get_absolute_url 方法返回的 URL
            return redirect(post)
        else: # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误
            print('bao cun bu cheng gong')

            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页
    print('get...')
    return redirect(post)
    # return HttpResponse('ok')
