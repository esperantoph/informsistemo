# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from informsistemo.main.models import AbstractTimeStampedModel


optional = {
    'blank': True,
    'null': True,
}


class Announcement(AbstractTimeStampedModel):
    """
    Model for managing organization-wide annoucements.
    """
    
    author = models.ForeignKey('users.User', related_name='posted_announcements')
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    body = models.TextField(verbose_name=_('Body'))
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, **optional)
    datetime_start = models.DateTimeField(verbose_name=_('Start'))
    datetime_end = models.DateTimeField(verbose_name=_('End'), **optional)
    notify_user = models.BooleanField(verbose_name=_('Notify User'), default=True)
    is_published = models.BooleanField(verbose_name=_('Is Published'), default=True)
    is_commentable = models.BooleanField(verbose_name=_('Is Commentable'), default=True)
    
    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        return super(Announcement, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title


class OrganizationEventManager(models.Manager):
    def get_queryset(self):
        return super(OrganizationEventManager, self).get_queryset().annotate(participants_count=Count('participants'))


class OrganizationEvent(AbstractTimeStampedModel):
    """
    Model for managing organization-wide events.
    """
    
    author = models.ForeignKey('users.User', related_name='posted_events')
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=255)
    detailed_description = models.TextField(verbose_name=_('Detailed Description'), **optional)
    location = models.CharField(verbose_name=_('Location'), max_length=255, **optional)
    datetime_start = models.DateTimeField(verbose_name=_('Start'))
    datetime_end = models.DateTimeField(verbose_name=_('End'), **optional)
    notify_user = models.BooleanField(verbose_name=_('Notify User'), default=True)
    is_published = models.BooleanField(verbose_name=_('Is Published'), default=True)
    is_commentable = models.BooleanField(verbose_name=_('Is Commentable'), default=True)
    participants = models.ManyToManyField('users.AssociateProfile',
                                          through='OrganizationEventParticipant',
                                          through_fields=('event', 'person'),
                                          verbose_name=_('Atendees'), blank=True)
    
    objects = OrganizationEventManager()
    
    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
    
    def total_participants(self):
        return self.participants_count
    total_participants.short_description = _('Atendees')
    total_participants.admin_order_field = 'participants_count'
    
    def render_month(self, date):
        return self.MONTHS[date]
    
    def render_datetime(self, d):
        return d.strftime('%d %b %Y, %I:%M %p')
    
    def render_datetime_duration(self):
        if self.datetime_end:
            return "{} - {}".format(self.render_datetime(self.datetime_start),
                                  self.render_datetime(self.datetime_end))
        return "{}".format(self.render_datetime(self.datetime_start))
    
    def __unicode__(self):
        return self.title


class OrganizationEventParticipant(AbstractTimeStampedModel):
    """
    Model for managing participants for organization-wide events.
    """
    
    event = models.ForeignKey(OrganizationEvent, on_delete=models.CASCADE)
    person = models.ForeignKey('users.AssociateProfile', on_delete=models.CASCADE)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                related_name="listed_event_participants")
    
    class Meta:
        verbose_name = _('Event Attendee')
        verbose_name_plural = _('Event Attendees')
        unique_together = ('event', 'person',)
    
    def __unicode__(self):
        return "added on {}".format(self.datetime_created)
