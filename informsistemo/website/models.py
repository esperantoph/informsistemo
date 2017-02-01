# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from colorfield.fields import ColorField
from redactor.fields import RedactorField

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
    
    ESPERANTO_GREEN = '#51bd20'
    
    homepage_title = models.CharField(verbose_name=_('Page Title'), max_length=50, default=_('Saluton!'), **optional)
    homepage_description_short = models.CharField(verbose_name=_('Page Description'), max_length=140, default=_('La oficiala retejo de la landa junulara Esperanto-organizo de Filipinoj.'), **optional)
    
    # main section
    main_navbar_text = models.CharField(verbose_name=_('Navbar Text'), max_length=15, default=_('Hello!'), **optional)
    main_navbar_shown = models.BooleanField(verbose_name=_('Display Link On Navbar'), default=False)
    main_header_text = models.CharField(verbose_name=_('Header'), max_length=50, default=_('Hello!'))
    main_description_short = RedactorField(verbose_name=_('Short Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    main_description_long = RedactorField(verbose_name=_('Long Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    main_header_image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, max_length=255, **optional)
    main_header_image_shown = models.BooleanField(verbose_name=_('Use Header Image'), default=False)
    main_header_color = ColorField(verbose_name=_('Background Color'), default=ESPERANTO_GREEN, **optional)
    main_header_div_id = models.SlugField(verbose_name=_('Element ID'), default=_('hello'), max_length=255, **optional)
    
    # about section
    about_navbar_text = models.CharField(verbose_name=_('Navbar Text'), max_length=15, default=_('About'), **optional)
    about_navbar_shown = models.BooleanField(verbose_name=_('Display Link On Navbar'), default=True)
    about_header_text = models.CharField(verbose_name=_('Header'), max_length=50, default=_('About'))
    about_description_short = RedactorField(verbose_name=_('Short Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    about_description_long = RedactorField(verbose_name=_('Long Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    about_header_image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, max_length=255, **optional)
    about_header_image_shown = models.BooleanField(verbose_name=_('Use Header Image'), default=False)
    about_header_color = ColorField(verbose_name=_('Background Color'), default=ESPERANTO_GREEN, **optional)
    about_header_div_id = models.SlugField(verbose_name=_('Element ID'), default=_('about'), max_length=255, **optional)
    about_button_text = models.CharField(verbose_name=_('Action Button Text'), default=_('Read more'), max_length=20, **optional)
    about_button_url = models.URLField(verbose_name=_('Action Button Link'), max_length=255, **optional)
    about_button_shown = models.BooleanField(verbose_name=_('Use Action Button'), default=False, blank=True)
    
    # contribute section
    contribute_navbar_text = models.CharField(verbose_name=_('Navbar Text'), max_length=15, default=_('Contribute'), **optional)
    contribute_navbar_shown = models.BooleanField(verbose_name=_('Display Link On Navbar'), default=True)
    contribute_header_text = models.CharField(verbose_name=_('Header'), max_length=50, default=_('Contribute'))
    contribute_description_short = RedactorField(verbose_name=_('Short Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    contribute_description_long = RedactorField(verbose_name=_('Long Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    contribute_header_image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, max_length=255, **optional)
    contribute_header_image_shown = models.BooleanField(verbose_name=_('Use Header Image'), default=False)
    contribute_header_color = ColorField(verbose_name=_('Background Color'), default=ESPERANTO_GREEN, **optional)
    contribute_header_div_id = models.SlugField(verbose_name=_('Element ID'), default=_('contribute'), max_length=255, **optional)
    contribute_button_text = models.CharField(verbose_name=_('Action Button Text'), default=_('Read more'), max_length=20, **optional)
    contribute_button_url = models.URLField(verbose_name=_('Action Button Link'), max_length=255, **optional)
    contribute_button_shown = models.BooleanField(verbose_name=_('Use Action Button'), default=False, blank=True)
    
    # contact section
    contact_navbar_text = models.CharField(verbose_name=_('Navbar Text'), max_length=15, default=_('Contact'), **optional)
    contact_navbar_shown = models.BooleanField(verbose_name=_('Display Link On Navbar'), default=True)
    contact_header_text = models.CharField(verbose_name=_('Header'), max_length=50, default=_('Contact'))
    contact_description_short = RedactorField(verbose_name=_('Short Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    contact_description_long = RedactorField(verbose_name=_('Long Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    contact_header_image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, max_length=255, **optional)
    contact_header_image_shown = models.BooleanField(verbose_name=_('Use Header Image'), default=False)
    contact_header_color = ColorField(verbose_name=_('Background Color'), default=ESPERANTO_GREEN, **optional)
    contact_header_div_id = models.SlugField(verbose_name=_('Element ID'), default=_('contact'), max_length=255, **optional)
    contact_button_text = models.CharField(verbose_name=_('Action Button Text'), default=_('Read more'), max_length=20, **optional)
    contact_button_url = models.URLField(verbose_name=_('Action Button Link'), max_length=255, **optional)
    contact_button_shown = models.BooleanField(verbose_name=_('Use Action Button'), default=False, blank=True)
    
    # articles
    articles_navbar_text = models.CharField(verbose_name=_('Navbar Text'), max_length=15, default=_('Contact'), **optional)
    articles_navbar_shown = models.BooleanField(verbose_name=_('Display Link On Navbar'), default=True)
    articles_header_text = models.CharField(verbose_name=_('Header'), max_length=50, default=_('Contact'))
    articles_description_short = RedactorField(verbose_name=_('Short Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    articles_description_long = RedactorField(verbose_name=_('Long Description'), allow_file_upload=False, allow_image_upload=False, **optional)
    articles_header_image = models.ImageField(verbose_name=_('Image'), upload_to=get_upload_path, max_length=255, **optional)
    articles_header_color = ColorField(verbose_name=_('Background Color'), default=ESPERANTO_GREEN, **optional)
    articles_header_div_id = models.SlugField(verbose_name=_('Element ID'), default=_('contact'), max_length=255, **optional)
    articles_button_text = models.CharField(verbose_name=_('Action Button Text'), default=_('Read more'), max_length=20, **optional)
    articles_button_url = models.URLField(verbose_name=_('Action Button Link'), max_length=255, **optional)
    articles_button_shown = models.BooleanField(verbose_name=_('Use Action Button'), default=False, blank=True)
    articles_limit_items = models.PositiveIntegerField(verbose_name=_('Limit # of Items'), default=3)
    
    # events
    # events_header_text = models.CharField(verbose_name=_('Header'), max_length=50,
    #                                       default=_('Recent Events'))
    # events_subtitle_text = models.TextField(verbose_name=_('Subtitle'), **optional)
    # events_limit_items = models.PositiveIntegerField(verbose_name=_('Limit # of Items'),
    #                                                  default=3)
    
    class Meta:
        verbose_name = _('Homepage Setting')
        verbose_name_plural = _('Homepage Settings')
    
    def __unicode__(self):
        return "{}".format(self.main_header_text)
    
    def save(self, *args, **kwargs):
        if not self.main_header_div_id:
            self.main_header_div_id = slugify(self.main_navbar_text)
        if not self.about_header_div_id:
            self.about_header_div_id = slugify(self.about_navbar_text)
        if not self.contribute_header_div_id:
            self.contribute_header_div_id = slugify(self.contribute_navbar_text)
        if not self.contact_header_div_id:
            self.contact_header_div_id = slugify(self.contact_navbar_text)
        if not self.articles_header_div_id:
            self.articles_header_div_id = slugify(self.articles_navbar_text)
            
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
