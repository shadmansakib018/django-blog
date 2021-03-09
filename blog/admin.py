from django.contrib import admin
from .models import Post
# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     '''
#         Admin View for Post
#     '''
#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)

admin.site.register(Post)