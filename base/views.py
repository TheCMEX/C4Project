# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from base.models import Board, Product, News


def homepage(request):
    return render(request, 'homepage.html')


def discuss(request):
    boards = Board.objects.all()
    return render(request, 'discuss.html', {'base': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})


def teams_c4(request):
    return render(request, 'teams_c4.html')


def teams_face2face(request):
    return render(request, 'teams_face2face.html')


def teams_isopromat(request):
    return render(request, 'teams_isopromat.html')


def achievements(request):
    return render(request, 'achievements.html')


def product(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'product.html', context)


def news(request):
    news = reversed(News.objects.all())

    context = {
        'news': news
    }
    return render(request, 'news.html', context)


def newspost(request, id):
    try:
        post = News.objects.get(id=id)
        previous_id = post.id - 1
        next_id = post.id + 1
        context = {
            'post': post,
            'previous_id': previous_id,
            'next_id': next_id,
            'max_id': len(News.objects.all()),
        }
        return render(request, 'newspost.html', context)

    except News.DoesNotExist:
        return render(request, 'errordne.html')

