# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ArticleListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.ArticleDetailView.as_view(),
        name='detail'
    ),
]
