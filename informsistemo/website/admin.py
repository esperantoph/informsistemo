# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from informsistemo.admin.basic_site import basic_admin_site

from .models import (
    Article,
    DailyQuotation,
    HomepageSetting,
    SocialAccount,
)


@admin.register(HomepageSetting)
class HomepageSettingAdmin(admin.ModelAdmin):
    """
    Manage Homepage Settings from the admin dashboard.
    """
    
    fieldsets = (
        (None, {
            'fields': (
                'homepage_title',
                'homepage_description_short',
            ),
        }),
        (_('Main Section'), {
            'classes': ('collapse',),
            'fields': (
                'main_navbar_text',
                'main_navbar_shown',
                'main_header_text',
                'main_description_short',
                'main_header_image',
                'main_header_color',
                'main_header_div_id',
            ),
        }),
        (_('About Section'), {
            'classes': ('collapse',),
            'fields': (
                'about_navbar_text',
                'about_navbar_shown',
                'about_header_text',
                'about_description_short',
                'about_header_image',
                'about_header_color',
                'about_header_div_id',
                'about_button_text',
                'about_button_url',
                'about_button_shown',
            ),
        }),
        (_('Contribute Section'), {
            'classes': ('collapse',),
            'fields': (
                'contribute_navbar_text',
                'contribute_navbar_shown',
                'contribute_header_text',
                'contribute_description_short',
                'contribute_header_image',
                'contribute_header_color',
                'contribute_header_div_id',
                'contribute_button_text',
                'contribute_button_url',
                'contribute_button_shown',
            ),
        }),
        (_('Contact Section'), {
            'classes': ('collapse',),
            'fields': (
                'contact_navbar_text',
                'contact_navbar_shown',
                'contact_header_text',
                'contact_description_short',
                'contact_header_image',
                'contact_header_color',
                'contact_header_div_id',
                'contact_button_text',
                'contact_button_url',
                'contact_button_shown',
            ),
        }),
        (_('Articles Section'), {
            'classes': ('collapse',),
            'fields': (
                'articles_navbar_text',
                'articles_navbar_shown',
                'articles_header_text',
                'articles_description_short',
                'articles_header_image',
                'articles_header_color',
                'articles_header_div_id',
                'articles_button_text',
                'articles_button_url',
                'articles_button_shown',
            ),
        }),
    )
    list_display = ('main_header_text', 'datetime_created',)


basic_admin_site.register(HomepageSetting, HomepageSettingAdmin)


@admin.register(DailyQuotation)
class DailyQuotationAdmin(admin.ModelAdmin):
    """
    View DailyQuotations from the admin dashboard.
    """
    
    # list_display = ('text', 'author', 'pub_date')
    # list_filter = ('datetime_created',)
    # search_fields = ('text', 'author',)
    
    pass


basic_admin_site.register(DailyQuotation, DailyQuotationAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    View Articles from the admin dashboard.
    """
    
    raw_id_fields = ('author',)
    fieldsets_user = (
        (_('Main Information'), {
            'fields': (
                'title',
                'body',
                'slug',
            )
        }),
        (_('Publishing Options'), {
            'classes': ('collapse',),
            'fields': (
                'datetime_published',
                'is_published',
                'is_commentable',
            )
        }),
    )
    fieldsets_superuser = (
        (_('Manage Author'), {
            'classes': ('collapse',),
            'fields': (
                'author',
            )
        }),
    )
    
    list_display = ('id', 'title', 'slug',)
    list_filter = ('datetime_published', 'is_published', 'is_commentable',)
    search_fields = ('title', 'body', 'slug',)
    prepopulated_fields = {"slug": ("title",)}
    
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        
        if request.user.is_superuser or request.user.is_manager:
            return qs
        return qs.filter(user=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if request.user.is_superuser:
            self.fieldsets = self.fieldsets_user + self.fieldsets_superuser
        else:
            self.fieldsets = self.fieldsets_user
        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)
    
    def get_changeform_initial_data(self, request):
        return {
            'author': request.user.pk,
            'datetime_published': timezone.now()
        }


basic_admin_site.register(Article, ArticleAdmin)


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    """
    View Milestones from the admin dashboard.
    """
    
    list_display = ('title', 'icon', 'url', 'datetime_created', 'order',)
    list_filter = ('datetime_created',)
    search_fields = ('title',)


basic_admin_site.register(SocialAccount, SocialAccountAdmin)

