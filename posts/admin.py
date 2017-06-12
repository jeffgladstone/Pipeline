from django.contrib import admin
from .models import Post, Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'post_date', 'account', 'votes')
    search_fields = ('message',)
    list_filter = ('post_date',)
    date_hierarchy = 'post_date'
    ordering = ('-post_date',)
    fields = ('message', 'post_date', 'account', 'votes')
    raw_id_fields = ('account',)

admin.site.register(Post, PostAdmin)
admin.site.register(Account, AccountAdmin)