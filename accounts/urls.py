from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from accounts import views as accounts_views


urlpatterns = [
    url(r'^signup/$', accounts_views.signup, name='signup'),
]