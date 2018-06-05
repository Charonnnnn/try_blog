from haystack import indexes
from .models import Post
'''
django-haystack 是一个专门提供搜索功能的 django 第三方应用，
它支持 Solr、Elasticsearch、Whoosh、Xapian 等多种搜索引擎，
配合著名的中文自然语言处理库 jieba 分词，就可以为博客提供一个效果不错的博客文章搜索系统

安装依赖: 
pip install whoosh django-haystack jieba
setting.py要设置
'''

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    '''
    document=True 代表django haystack和搜索引擎将使用此字段的内容作为索引进行检索(primary field)
    use_template=True 允许我们使用数据模板去建立搜索引擎索引的文件 {{ ... }}
    '''

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()