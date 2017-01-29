# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as AuthUserAdmin,
    GroupAdmin as AuthGroupAdmin,
)
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from informsistemo.admin.basic_site import basic_admin_site

from .models import User, MemberProfile



class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': ('name',)}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'is_superuser')
    search_fields = ['name']


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    """
    Admin for the MemberProfile.
    """
    
    raw_id_fields = ('user',)
    fieldsets_user = (
        (_('Personal Information'), {
            'fields': (
                'name_title',
                'first_name',
                'middle_name',
                'last_name',
                'name_suffix',
                'nick_name',
                'sex',
                'birthdate',
                'civil_status',
                'nationality',
                'occupation',
                'location',
            )
        }),
        (_('Personal Contact Information'), {
            'fields': (
                'personal_address',
                'personal_telephone',
                'personal_mobile',
                'personal_email',
            )
        }),
        (_('Business Contact Information'), {
            'classes': ('collapse',),
            'fields': (
                'business_address',
                'business_telephone',
                'business_mobile',
                'business_email',
            )
        }),
    )
    fieldsets_superuser = (
        (_('User Account Information'), {
            'classes': ('collapse',),
            'fields': (
                'user',
            )
        }),
    )
    
    list_display = ('last_name', 'first_name', 'sex', 'calculate_age',
                    'location', 'personal_mobile',)
    list_filter = ('sex', 'civil_status',)
    search_fields = ('id', 'last_name', 'first_name', 'middle_name', 'name_suffix', 'nick_name',
                     'birthdate', 'location',)
    
    def get_queryset(self, request):
        qs = super(MemberProfileAdmin, self).get_queryset(request)
        
        if request.user.is_superuser or request.user.is_manager:
            return qs
        return qs.filter(user=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if request.user.is_superuser:
            self.fieldsets = self.fieldsets_user + self.fieldsets_superuser
        else:
            self.fieldsets = self.fieldsets_user
        return super(MemberProfileAdmin, self).get_form(request, obj, **kwargs)


basic_admin_site.register(User, MyUserAdmin)
basic_admin_site.register(MemberProfile, MemberProfileAdmin)
basic_admin_site.register(Group, AuthGroupAdmin)
