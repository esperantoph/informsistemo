# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from informsistemo.admin.basic_site import basic_admin_site

from .models import Announcement


optional = {
    'blank': True,
    'null': True,
}


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    """
    Admin for the Announcement.
    """
    
    raw_id_fields = ('author',)
    fieldsets_user = (
        (_('Main Information'), {
            'fields': (
                'title',
                'slug',
                'body',
            )
        }),
        (_('Publishing Options'), {
            'classes': ('collapse',),
            'fields': (
                'datetime_start',
                'datetime_end',
                'is_published',
                'is_commentable',
            )
        }),
    )
    fieldsets_superuser = (
        (_('User Account Information'), {
            'classes': ('collapse',),
            'fields': (
                'author',
                'notify_user',
            )
        }),
    )
    
    list_display = ('id', 'title', 'slug',)
    list_filter = ('is_published', 'is_commentable',)
    search_fields = ('title', 'slug', 'body',)
    
    def get_queryset(self, request):
        qs = super(AnnouncementAdmin, self).get_queryset(request)
        
        if request.user.is_superuser or request.user.is_manager:
            return qs
        return qs.filter(user=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if request.user.is_superuser:
            self.fieldsets = self.fieldsets_user + self.fieldsets_superuser
        else:
            self.fieldsets = self.fieldsets_user
        return super(AnnouncementAdmin, self).get_form(request, obj, **kwargs)


# basic_admin_site.register(Announcement, AnnouncementAdmin)
