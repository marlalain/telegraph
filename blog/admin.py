from django.contrib import admin

from .models import Link, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(Link)
admin.site.register(Post, PostAdmin)
