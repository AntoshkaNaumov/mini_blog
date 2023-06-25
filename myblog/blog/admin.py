#from django.contrib import admin
#from .models import Post, Comments


#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author')


#@admin.register(Comments)
#class CommentsAdmin(admin.ModelAdmin):
#    list_display = ('name', 'post')

from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_comments', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
