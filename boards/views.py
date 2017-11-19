# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from boards.models import Board


def homepage(request):
    return render(request, 'homepage.html')


def discuss(request):
    boards = Board.objects.all()
    return render(request, 'discuss.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
