from django.contrib import admin

# Register your models here.

from .models import Comment
from .models import Settings

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', "content")

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('setting', "value")

admin.site.register(Comment, CommentAdmin)
admin.site.register(Settings, SettingsAdmin)
