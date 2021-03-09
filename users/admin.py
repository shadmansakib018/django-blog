from django.contrib import admin
from .models import Profile
# Register your models here.
# class Admin(admin.ModelAdmin):
#     '''
#         Admin View for 
#     '''
#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)

admin.site.register(Profile)