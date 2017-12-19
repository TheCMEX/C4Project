# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import math
from markdown import markdown
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import Truncator


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.name, self.description)

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, int(count + 1))

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))


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


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=250, verbose_name='Описание', default='Описание')
    text = models.TextField(verbose_name='Текст новости')
    photo = models.ImageField(blank=True, upload_to='media/images/news/%Y/%m/%d', help_text='200x200px',
                              verbose_name='Ссылка картинки')
    date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'

    def image_img(self):
        if self.photo:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.photo.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
