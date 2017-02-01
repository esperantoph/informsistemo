# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 14:59
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import informsistemo.main.utils.modelutils
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20170129_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('datetime_updated', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
                ('datetime_published', models.DateTimeField(verbose_name='Date Published')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is Published')),
                ('is_commentable', models.BooleanField(default=True, verbose_name='Is Commentable')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='users.MemberProfile', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='DailyQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('datetime_updated', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('text', models.TextField(verbose_name='Text')),
                ('author', models.CharField(blank=True, max_length=30, null=True, verbose_name='Author')),
                ('pub_date', models.DateField(unique=True, verbose_name='For Date')),
            ],
            options={
                'verbose_name': 'Daily Quotation',
                'verbose_name_plural': 'Daily Quotations',
            },
        ),
        migrations.CreateModel(
            name='HomepageSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('datetime_updated', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('homepage_title', models.CharField(blank=True, default='Saluton!', max_length=50, null=True, verbose_name='Page Title')),
                ('homepage_description_short', models.CharField(blank=True, default='La oficiala retejo de la landa junulara Esperanto-organizo de Filipinoj.', max_length=140, null=True, verbose_name='Page Description')),
                ('main_navbar_text', models.CharField(blank=True, default='Hello!', max_length=15, null=True, verbose_name='Navbar Text')),
                ('main_navbar_shown', models.BooleanField(default=False, verbose_name='Display Link On Navbar')),
                ('main_header_text', models.CharField(default='Hello!', max_length=50, verbose_name='Header')),
                ('main_description_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Description')),
                ('main_description_long', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Long Description')),
                ('main_header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('main_header_image_shown', models.BooleanField(default=False, verbose_name='Use Header Image')),
                ('main_header_color', colorfield.fields.ColorField(blank=True, default='#51bd20', max_length=10, null=True, verbose_name='Background Color')),
                ('main_header_div_id', models.SlugField(blank=True, default='hello', max_length=255, null=True, verbose_name='Element ID')),
                ('about_navbar_text', models.CharField(blank=True, default='About', max_length=15, null=True, verbose_name='Navbar Text')),
                ('about_navbar_shown', models.BooleanField(default=True, verbose_name='Display Link On Navbar')),
                ('about_header_text', models.CharField(default='About', max_length=50, verbose_name='Header')),
                ('about_description_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Description')),
                ('about_description_long', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Long Description')),
                ('about_header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('about_header_image_shown', models.BooleanField(default=False, verbose_name='Use Header Image')),
                ('about_header_color', colorfield.fields.ColorField(blank=True, default='#51bd20', max_length=10, null=True, verbose_name='Background Color')),
                ('about_header_div_id', models.SlugField(blank=True, default='about', max_length=255, null=True, verbose_name='Element ID')),
                ('about_button_text', models.CharField(blank=True, default='Read more', max_length=20, null=True, verbose_name='Action Button Text')),
                ('about_button_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Action Button Link')),
                ('about_button_shown', models.BooleanField(default=False, verbose_name='Use Action Button')),
                ('contribute_navbar_text', models.CharField(blank=True, default='Contribute', max_length=15, null=True, verbose_name='Navbar Text')),
                ('contribute_navbar_shown', models.BooleanField(default=True, verbose_name='Display Link On Navbar')),
                ('contribute_header_text', models.CharField(default='Contribute', max_length=50, verbose_name='Header')),
                ('contribute_description_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Description')),
                ('contribute_description_long', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Long Description')),
                ('contribute_header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('contribute_header_image_shown', models.BooleanField(default=False, verbose_name='Use Header Image')),
                ('contribute_header_color', colorfield.fields.ColorField(blank=True, default='#51bd20', max_length=10, null=True, verbose_name='Background Color')),
                ('contribute_header_div_id', models.SlugField(blank=True, default='contribute', max_length=255, null=True, verbose_name='Element ID')),
                ('contribute_button_text', models.CharField(blank=True, default='Read more', max_length=20, null=True, verbose_name='Action Button Text')),
                ('contribute_button_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Action Button Link')),
                ('contribute_button_shown', models.BooleanField(default=False, verbose_name='Use Action Button')),
                ('contact_navbar_text', models.CharField(blank=True, default='Contact', max_length=15, null=True, verbose_name='Navbar Text')),
                ('contact_navbar_shown', models.BooleanField(default=True, verbose_name='Display Link On Navbar')),
                ('contact_header_text', models.CharField(default='Contact', max_length=50, verbose_name='Header')),
                ('contact_description_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Description')),
                ('contact_description_long', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Long Description')),
                ('contact_header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('contact_header_image_shown', models.BooleanField(default=False, verbose_name='Use Header Image')),
                ('contact_header_color', colorfield.fields.ColorField(blank=True, default='#51bd20', max_length=10, null=True, verbose_name='Background Color')),
                ('contact_header_div_id', models.SlugField(blank=True, default='contact', max_length=255, null=True, verbose_name='Element ID')),
                ('contact_button_text', models.CharField(blank=True, default='Read more', max_length=20, null=True, verbose_name='Action Button Text')),
                ('contact_button_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Action Button Link')),
                ('contact_button_shown', models.BooleanField(default=False, verbose_name='Use Action Button')),
                ('articles_navbar_text', models.CharField(blank=True, default='Contact', max_length=15, null=True, verbose_name='Navbar Text')),
                ('articles_navbar_shown', models.BooleanField(default=True, verbose_name='Display Link On Navbar')),
                ('articles_header_text', models.CharField(default='Contact', max_length=50, verbose_name='Header')),
                ('articles_description_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Description')),
                ('articles_description_long', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Long Description')),
                ('articles_header_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=informsistemo.main.utils.modelutils.get_upload_path, verbose_name='Image')),
                ('articles_header_color', colorfield.fields.ColorField(blank=True, default='#51bd20', max_length=10, null=True, verbose_name='Background Color')),
                ('articles_header_div_id', models.SlugField(blank=True, default='contact', max_length=255, null=True, verbose_name='Element ID')),
                ('articles_button_text', models.CharField(blank=True, default='Read more', max_length=20, null=True, verbose_name='Action Button Text')),
                ('articles_button_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Action Button Link')),
                ('articles_button_shown', models.BooleanField(default=False, verbose_name='Use Action Button')),
                ('articles_limit_items', models.PositiveIntegerField(default=3, verbose_name='Limit # of Items')),
            ],
            options={
                'verbose_name': 'Homepage Setting',
                'verbose_name_plural': 'Homepage Settings',
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('datetime_updated', models.DateTimeField(editable=False, verbose_name='Modified')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('icon', models.CharField(max_length=30, verbose_name='Font Awesome Icon')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('order', models.IntegerField(default=1, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
            },
        ),
    ]
