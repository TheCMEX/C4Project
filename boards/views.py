# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from boards.models import Board


def homepage(request):
    return render(request, 'homepage.html')


def discuss(request):
    boards = Board.objects.all()
    return render(request, 'discuss.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})

