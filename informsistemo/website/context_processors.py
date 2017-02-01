# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from informsistemo.website.models import (
    HomepageSetting,
    SocialAccount,
    DailyQuotation,
)


def homepage_settings(request):
    """
    Context processor for adding the homepage settings to the context.
    """
    return {
        'social_accounts': SocialAccount.objects.all().order_by('order'),
        'hs': HomepageSetting.objects.first(),
        'daily_quote': DailyQuotation.objects.get_today_or_last(),
    }
