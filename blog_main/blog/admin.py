from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Tag, Comment
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag, TagAdmin)
