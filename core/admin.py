from django.contrib import admin
from core.models import Post, Comment, Like, Follow, SavedPost

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'image', 'user', 'created_on', 'updated_on']


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'post', 'user', 'commented_on', 'updated_on']


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'liked_on', 'updated_on']


@admin.register(Follow)
class FollowModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'followed',  'followed_on', 'updated_on']


@admin.register(SavedPost)
class SavedPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'saved_on']



