# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Board, Product, News


class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name', 'description']

    class Meta:
        model = Board


admin.site.register(Board, BoardAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fields = ['name', 'description', 'photo']


admin.site.register(Product, ProductAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo']


admin.site.register(News, NewsAdmin)



















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