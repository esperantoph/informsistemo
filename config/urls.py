# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from informsistemo.admin.basic_site import basic_admin_site
from informsistemo.website import views as website_views


urlpatterns = [
    url(r'^$', website_views.home_page, name='landing'),
    # url(r'^$', TemplateView.as_view(template_name='pages/landing.html'), name='landing'),
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, basic_admin_site.urls),
    
    # User management
    # url(r'^users/', include('informsistemo.users.urls', namespace='users')),
    url(r'^news/', include('informsistemo.website.urls', namespace='news')),
    url(r'^accounts/', include('allauth.urls')),
    
    # Your stuff: custom urls includes go here
    url(r'^redactor/', include('redactor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(regex=r'^400/$',
            view=default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        url(regex=r'^403/$',
            view=default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(regex=r'^404/$',
            view=default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        url(regex=r'^500/$',
            view=default_views.server_error),
    ]
    
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
