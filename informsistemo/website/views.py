# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.generic import (
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
)

from .models import (
    Article,
    HomepageSetting,
    SocialAccount,
)


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


class HomePageView(TemplateView):
    """
    View for the home/landing page.
    """
    
    template_name = 'pages/landing.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        
        hs = HomepageSetting.objects.all().first()
        if hs:
            context['featured_articles'] = Article.objects.filter(is_published=True).order_by('datetime_published')[:hs.articles_limit_items]
            
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)

home_page = HomePageView.as_view()
