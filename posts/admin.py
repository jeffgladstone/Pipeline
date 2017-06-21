from django.contrib import admin
from .models import Post, Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'post_date', 'user', 'votes')
    search_fields = ('message',)
    list_filter = ('post_date',)
    date_hierarchy = 'post_date'
    ordering = ('-post_date',)
    fields = ('message', 'post_date', 'user', 'votes')
    raw_id_fields = ('user',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar')
    search_fields = ('bio',)
    list_filter = ('user',)
    fields = ('user', 'bio', 'avatar')
    raw_id_fields = ('user',)



admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)


