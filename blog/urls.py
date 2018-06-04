
from django.urls import path,re_path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('index/',views.index,name = 'index'),
    re_path('post/(?P<pk>[0-9]+)/',views.detail,name='detail'),
    # (?P<name>…)带命名的组
    # [0-9]+表示一位或者多位数. (?P<pk>[0-9]+)表示命名捕获组, 其作用是从用户访问的URL里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/',views.arhchives, name='archives'),
    re_path('category/(?P<pk>[0-9]+)/', views.category, name='category'),

]
