# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.name, self.description)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')


# class Team(models.Model):
#     team_name = models.CharField(max_length=25, unique=True)
#     player = models.CharField(max_length=25, unique=True)
#     player1 = models.CharField(max_length=25, unique=True)
#     player2 = models.CharField(max_length=25, unique=True)
#     player3 = models.CharField(max_length=25, unique=True)
#     player4 = models.CharField(max_length=25, unique=True)
#     player5 = models.CharField(max_length=25, unique=True)
#     player6 = models.CharField(max_length=25, unique=True)
#     player7 = models.CharField(max_length=25, unique=True)
#     player8 = models.CharField(max_length=25, unique=True)
#
#     def __str__(self):
#         return "%s %s %s %s %s %s %s %s %s %s" % (
#             self.team_name, self.player, self.player1, self.player2, self.player3, self.player4, self.player5,
#             self.player6,
#             self.player7, self.player8)

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Товар')
    description = models.CharField(max_length=100, verbose_name='Описание', default='Описание')
    photo = models.ImageField(upload_to='../../static/media/images/products/%Y/%m/%d', null=False, blank=True,
                              verbose_name='Изображение',  help_text='150x150px')

    def __str__(self):
        return '%s %s %s' % (self.name, self.description, self.photo)


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=250, verbose_name='Описание', default='Описание')
    text = models.TextField(verbose_name='Текст новости')
    photo = models.ImageField(upload_to='../../static/media/images/news/%Y/%m/%d', blank=True,
                              verbose_name='Изображение', help_text='150x150px')
    date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
