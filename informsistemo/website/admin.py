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
    
    # fieldsets = (
    #     (_('Main'), {
    #         'fields': (
    #             'main_header_text',
    #             'main_header_image',
    #             'main_subtitle_text',
    #             'main_description_text',
    #         ),
    #     }),
    #     (_('Articles Section'), {
    #         'fields': (
    #             'articles_header_text',
    #             'articles_subtitle_text',
    #             'articles_subtitle_text2',
    #             'articles_limit_items',
    #         ),
    #     }),
    #     (_('Contact Section'), {
    #         'fields': (
    #             'contact_header_text',
    #             'contact_subtitle_text',
    #         ),
    #     }),
    # )
    # list_display = ('main_header_text', 'datetime_created',)
    
    pass


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
    
    # list_display = ('title', 'icon', 'url', 'datetime_created', 'order',)
    # list_filter = ('datetime_created',)
    # search_fields = ('title',)
    
    pass


basic_admin_site.register(SocialAccount, SocialAccountAdmin)

