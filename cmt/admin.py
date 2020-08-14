from django.contrib import admin
from .models import Cmt

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post_title','date')
    list_display_links = ('id','post_title')
    search_fields = ('post_title', 'comment')
    list_per_page = 10

admin.site.register(Cmt, CommentAdmin)
