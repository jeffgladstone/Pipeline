from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'post_date', 'user', 'votes')
    search_fields = ('message',)
    list_filter = ('post_date',)
    date_hierarchy = 'post_date'
    ordering = ('-post_date',)
    fields = ('message', 'post_date', 'user', 'votes')
    raw_id_fields = ('user',)



admin.site.register(Post, PostAdmin)

