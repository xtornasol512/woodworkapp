from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

from core.behaviors import Timestampable


class Company(Timestampable, models.Model):
    ''' Company model '''

    title = models.CharField("Title", max_length=255, default="")
    phone = models.CharField("Phone", max_length=50, blank=True, default="")
    fax = models.CharField("Fax", max_length=255, blank=True, default="")
    email = models.EmailField("Email", max_length=255, blank=True)
    headline = models.CharField("Headline", max_length=255, blank=True, default="")
    address = models.CharField("Address", max_length=255, blank=True, default="")
    facebook = models.CharField("Facebook", max_length=255, blank=True, default="")
    twitter = models.CharField("Twitter", max_length=255, blank=True, default="")
    linkedin = models.CharField("Linkedin", max_length=255, blank=True, default="")
    instagram = models.CharField("Instagram", max_length=255, blank=True, default="")
    youtube = models.CharField("Youtube", max_length=255,  blank=True, default="")
    service_area = models.TextField("Service area", blank=True, default="")
    hours_operation = models.TextField("Hours of operation", blank=True, default="")
    main_video = models.URLField("Youtube or vimeo URL", blank=True)
    data = JSONField(blank=True, default={}, help_text="Metadata")

    class Meta:
        ''' Custom Admin metadata'''
        verbose_name_plural = "Company Settings"
        ordering = ['created_at']

    def __str__(self):
        ''' Display name to object '''
        return self.title

    @property
    def get_video_id(self):
        ''' Get the ID for url link '''
        return self.main_video.split("/")[-1]


class Client(Timestampable, models.Model):
    ''' Client Model '''
    name = models.CharField("Client name", max_length=255, default="")
    website = models.URLField("Website url", blank=True, max_length=255)
    headline = models.CharField("Company headline", max_length=255, blank=True, default="")
    logo = models.ImageField(upload_to='alliances_logos', blank=True)

    data = JSONField(blank=True, default={}, help_text="Metadata")

    def __str__(self):
        ''' Display name to object '''
        return self.name


class Quote(Timestampable, models.Model):
    ''' Quote model '''

    name = models.CharField("Lead name", max_length=255)
    email = models.EmailField("Email", max_length=255, blank=True)
    phone = models.CharField("Phone", max_length=50, blank=True, default="")
    company = models.CharField("Company name", max_length=255, default="")
    project = models.CharField("Project name", max_length=255, blank=True, default="")
    bid_due = models.DateField("Estimated start date", default=datetime.today)
    start_date = models.DateField("Estimated start date", default=datetime.today)
    PREVAILING_OPTIONS = (
        ("YES", 'YES'),
        ("NO", 'NO')
    )
    prevailing_wage = models.CharField("Prevailing wage", max_length=255, blank=True, choices=PREVAILING_OPTIONS, default="")
    description = models.TextField("Description", blank=True, default="")

    class Meta:
        ''' Custom Admin metadata'''
        verbose_name_plural = "Request Quotes"
        ordering = ['created_at']

    def __str__(self):
        ''' Display name to object '''
        return self.name

    def clean_start_date(self, value):
        ''' Custom validate start date field '''
        print("[custom validation field ] Value: {}".format(value))

