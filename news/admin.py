from django.contrib import admin, messages
from .models import Article, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('commenter', 'body', 'article', 'created_on', 'approved')
    search_fields = ['commenter', 'email', 'body']
    actions = ['approve_comments']

    @admin.action(description='Mark selected comment(s) as approved?')
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('completed', 'created_on')
    list_display = ('name', 'email', 'subject', 'created_on', 'completed')
    search_fields = ['name', 'email',]
    actions = ['completed']