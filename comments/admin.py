from django.contrib import admin
from comments import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']

admin.site.register(models.Comment,CommentAdmin)



