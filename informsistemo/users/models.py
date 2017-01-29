# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from informsistemo.main.models import AbstractTimeStampedModel
from informsistemo.main.utils.modelutils import get_upload_path


optional = {
    'blank': True,
    'null': True,
}


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class MemberProfileManager(models.Manager):
    def get_birthdays_within(self, x):
        today = date.today()
        x_days = today + timedelta(days=x)
        
        extra_month_query = 'EXTRACT(MONTH FROM users_memberprofile.birthdate)'
        extra_day_query = 'EXTRACT(DAY FROM users_memberprofile.birthdate)'
        
        queryset = self.get_queryset()
        
        if x == 0:  # today
            queryset = queryset.filter(
                birthdate__month=today.month,
                birthdate__day=today.day
            )
        elif x == 30:  # this month
            queryset = queryset.filter(
                birthdate__month=today.month,
                birthdate__day__gt=today.day
            )
        else:  # within 7 days
            if today.month == x_days.month:
                queryset = queryset.filter(
                    birthdate__month=today.month,
                    birthdate__day__gt=today.day,
                    birthdate__day__lte=x_days.day
                )
            else:
                queryset = queryset.filter(
                    Q(birthdate__month=today.month, birthdate__day__gt=today.day) |
                    Q(birthdate__month=x_days.month, birthdate__day__lte=x_days.day)
                )
        
        queryset = queryset.extra(select={'birthdate__month': extra_month_query,
                                          'birthdate__day': extra_day_query,
                                  })
        
        return queryset.select_related('user').order_by('birthdate__month',
                                                        'birthdate__day')
    
    def get_birthdays_today(self):
        return self.get_birthdays_within(0)
    
    def get_birthdays_next_week(self):
        return self.get_birthdays_within(7)
    
    def get_birthdays_next_month(self):
        return self.get_birthdays_within(30)


class MemberProfile(AbstractTimeStampedModel):
    """
    This is the main profile for the user accounts.
    """
    
    SEX_MALE = 1
    SEX_FEMALE = 2
    SEX_CHOICES = (
        (SEX_MALE, _('Male')),
        (SEX_FEMALE, _('Female')),
    )
    
    CIVIL_STATUS_SINGLE = 1
    CIVIL_STATUS_MARRIED = 2
    CIVIL_STATUS_WIDOWED = 3
    CIVIL_STATUS_SEPARATED_DIVORCED = 4
    CIVIL_STATUS_CHOICES = (
        (CIVIL_STATUS_SINGLE, _('Single')),
        (CIVIL_STATUS_MARRIED, _('Married')),
        (CIVIL_STATUS_WIDOWED, _('Widowed')),
        (CIVIL_STATUS_SEPARATED_DIVORCED, _('Separated/Divorced')),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", **optional)
    name_title = models.CharField(verbose_name=_('Title'), max_length=30, blank=True)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=35)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=35)
    middle_name = models.CharField(verbose_name=_('Middle Name'), max_length=35, blank=True)
    name_suffix = models.CharField(verbose_name=_('Suffix'), max_length=30, blank=True)
    nick_name = models.CharField(verbose_name=_('Nickname'), max_length=30, blank=True)
    
    birthdate = models.DateField(verbose_name=_('Birthdate'))
    birth_place = models.CharField(verbose_name=_('Birth Place'), max_length=255, **optional)
    sex = models.PositiveIntegerField(verbose_name=_('Sex'), choices=SEX_CHOICES, **optional)
    
    civil_status = models.PositiveIntegerField(verbose_name=_('Civil Status'),
                                                        choices=CIVIL_STATUS_CHOICES,
                                                        default=CIVIL_STATUS_SINGLE,
                                                        **optional)
    nationality = models.CharField(verbose_name=_('Nationality'), max_length=30,
                                   default=_('Filipino'), **optional)
    occupation = models.CharField(verbose_name=_('Occupation'), max_length=30, **optional)
    location = models.CharField(verbose_name=_('Location'), max_length=30, **optional)
    
    personal_address = models.TextField(verbose_name=_('Address'), **optional)
    personal_telephone = models.CharField(verbose_name=_('Telephone #'), max_length=30, **optional)
    personal_mobile = models.CharField(verbose_name=_('Mobile #'), max_length=30, **optional)
    personal_email = models.EmailField(verbose_name=_('Email Address'), **optional)
    
    business_address = models.TextField(verbose_name=_('Address'), **optional)
    business_telephone = models.CharField(verbose_name=_('Telephone #'), max_length=30, **optional)
    business_mobile = models.CharField(verbose_name=_('Mobile #'), max_length=30, **optional)
    business_email = models.EmailField(verbose_name=_('Email Address'), **optional)
    
    objects = MemberProfileManager()
    
    class Meta:
        verbose_name = _('Member Profile')
        verbose_name_plural = _('Member Profiles')
    
    def render_full_name(self):
        if self.first_name and self.last_name:
            full_name = "{} {}".format(self.first_name, self.last_name)
        else:
            return ""
        
        if self.name_suffix:
            full_name = "{} {}".format(full_name, self.name_suffix)
        
        if self.name_title:
            full_name = "{} {}".format(self.name_title, full_name)
        
        return full_name
    
    @property
    def full_name(self):
        return self.render_full_name()
    
    def render_sex(self):
        if self.sex == self.SEX_MALE:
            return _('Male')
        elif self.sex == self.SEX_FEMALE:
            return _('Female')
        else:
            return ''
    
    def calculate_age(self):
        if not self.birthdate:
            return None
        
        born = self.birthdate
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    calculate_age.short_description = _('Age')
    calculate_age.admin_order_field = 'birthdate'
    
    def get_admin_url(self):
        """the url to the Django admin interface for the model instance"""
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))
    
    def __str__(self):
        return '{}'.format(self.full_name)
