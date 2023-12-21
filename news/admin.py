from django.contrib import admin, messages
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'votes_total')
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'article', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    @admin.action(description='Mark selected comment(s) as approved?')
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
