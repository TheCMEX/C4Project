# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Board, News, Post, Topic


class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name', 'description']

    class Meta:
        model = Board


admin.site.register(Board, BoardAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'image_img']


admin.site.register(News, NewsAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['topic', 'message', 'created_by', 'created_at']
    list_filter = ['created_by', 'created_at', 'topic']
    search_fields = ['topic', 'message', 'created_by', 'created_at']


admin.site.register(Post, PostAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['subject', 'starter']


admin.site.register(Topic, TopicAdmin)















#
# class TeamAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Team._meta.fields]
#     search_fields = [field.name for field in Team._meta.fields]
#
#     class Meta:
#         model = Team
#
#
# admin.site.register(Team, TeamAdmin)