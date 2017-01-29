# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from informsistemo.main.models import AbstractTimeStampedModel
from informsistemo.main.utils.modelutils import get_upload_path


optional = {
    'blank': True,
    'null': True,
}


class HomepageSetting(AbstractTimeStampedModel):
    """
    Model for managing the homepage of the website.
    """
    
    # main
    main_header_text = models.CharField(verbose_name=_('Header'), max_length=50,
                                        default=_("Hello!"))
    main_header_image = models.ImageField(verbose_name=_('Image'),
                                          upload_to=get_upload_path, **optional)
    main_subtitle_text = models.TextField(verbose_name=_('Short Description'), **optional)
    main_description_text = models.TextField(verbose_name=_('Long Description'), **optional)
    
    # events
    events_header_text = models.CharField(verbose_name=_('Header'), max_length=50,
                                          default=_("Recent Events"))
    events_subtitle_text = models.TextField(verbose_name=_('Subtitle'), **optional)
    events_limit_items = models.PositiveIntegerField(verbose_name=_('Limit # of Items'),
                                                     default=3)
    
    # articles
    articles_header_text = models.CharField(verbose_name=_('Header'), max_length=50,
                                            default=_("Featured Articles"))
    articles_subtitle_text = models.TextField(verbose_name=_('Subtitle'), **optional)
    articles_subtitle_text2 = models.TextField(verbose_name=_('Subtitle 2'), **optional)
    articles_limit_items = models.PositiveIntegerField(verbose_name=_('Limit # of Items'),
                                                       default=3)
    
    # contact
    contact_header_text = models.CharField(verbose_name=_('Header'), max_length=50,
                                           default=_("Contact Us"))
    contact_subtitle_text = models.TextField(verbose_name=_('Subtitle'), **optional)
    
    class Meta:
        verbose_name = _('Homepage Setting')
        verbose_name_plural = _('Homepage Settings')
    
    def __unicode__(self):
        return "{}".format(self.main_header_text)
    
    def save(self, *args, **kwargs):
        return super(HomepageSetting, self).save(*args, **kwargs)


class DailyQuotationManager(models.Manager):
    """
    Model for managing the daily quotes
    """
    
    def get_today_or_last(self):
        today = timezone.now().date()
        q_today = self.filter(pub_date=today).last()
        return q_today if q_today is not None else self.last()


class DailyQuotation(AbstractTimeStampedModel):
    """
    Model for managing the daily quotes of the website.
    """
    
    text = models.TextField(verbose_name=_('Text'))
    author = models.CharField(verbose_name=_('Author'), max_length=30, **optional)
    pub_date = models.DateField(verbose_name=_('For Date'), unique=True)
    
    objects = DailyQuotationManager()
    
    class Meta:
        verbose_name = _('Daily Quotation')
        verbose_name_plural = _('Daily Quotations')
    
    def __unicode__(self):
        return "{}".format(self.text)


class Article(AbstractTimeStampedModel):
    """
    Model for managing the articles in the site.
    """
    
    title = models.CharField(verbose_name=_('Title'), max_length=30)
    author = models.ForeignKey('users.MemberProfile', verbose_name=_('Author'),
                               related_name='articles', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, **optional)
    body = models.TextField(verbose_name=_('Body'), **optional)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, **optional)
    datetime_published = models.DateTimeField(verbose_name=_('Date Published'))
    is_published = models.BooleanField(verbose_name=_('Is Published'), default=True)
    is_commentable = models.BooleanField(verbose_name=_('Is Commentable'), default=True)
    
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
    
    def __unicode__(self):
        return "{}".format(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        return super(Article, self).save(*args, **kwargs)


class SocialAccount(AbstractTimeStampedModel):
    """
    Model for managing the social accounts in the site.
    """
    
    title = models.CharField(verbose_name=_('Title'), max_length=30)
    icon  = models.CharField(verbose_name=_('Font Awesome Icon'), max_length=30)
    url = models.URLField(verbose_name=_('URL'), max_length=255)
    order = models.IntegerField(verbose_name=_('Order'), default=1)
    
    class Meta:
        verbose_name = _('Social Account')
        verbose_name_plural = _('Social Accounts')
    
    def __unicode__(self):
        return "{}".format(self.title)
