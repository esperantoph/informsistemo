# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite


class BasicAdminSite(AdminSite):
    site_header = 'FEJ Admin Dashboard'
    site_title = 'FEJ Admin Dashboard'


basic_admin_site = BasicAdminSite(name='basic_admin')
