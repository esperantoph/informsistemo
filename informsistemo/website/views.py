# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'article'
    template_name = 'website/news_detail.html'


class ArticleListView(ListView):
    model = Article
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'articles'
    template_name = 'website/news_list.html'
