# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import discuss

class DiscussTests(TestCase):
    def test_discuss_view_status_code(self):
        url = reverse('discuss')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_discuss_url_resolves_discuss_view(self):
        view = resolve('discuss')
        self.assertEquals(view.func, discuss)