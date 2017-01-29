# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


optional = {
    'blank': True,
    'null': True,
}


class AbstractTimeStampedModel(models.Model):
    """
    Base for time-stamped models.
    """
    
    datetime_created = models.DateTimeField(verbose_name=_('Created'), editable=False)
    datetime_updated = models.DateTimeField(verbose_name=_('Modified'), editable=False)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        # check if the instace already has an id
        if not self.id:
            self.datetime_created = timezone.now()
        
        # update date modified
        self.datetime_updated = timezone.now()
        
        return super(AbstractTimeStampedModel, self).save(*args, **kwargs)
