from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from core.behaviors import Timestampable

class Review(Timestampable, models.Model):
    ''' Review Model '''
    name = models.CharField("Reviewer name", max_length=255, default="")
    description = models.TextField(blank=True, default="")
    place = models.CharField("Place name", blank=True, max_length=255, default="", help_text='Square Image MIN_SIZE=320x320, MAX_SIZE=900x900')

    avatar = models.ImageField(upload_to='avatars')
    # avatar_thumbnail = ImageSpecField(source='avatar',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})

    def __str__(self):
        ''' Get name '''
        return self.name


class Tag(Timestampable, models.Model):
    ''' Tag table '''
    name = models.CharField("Tag name", max_length=255, default="", help_text="Prefer use without spaces (Could be with  '_' or '-')")
    description = models.CharField("Short description", blank=True, max_length=255, default="")

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Photo Tags"
        ordering = ['created_at']

    def __str__(self):
        ''' Return string data '''
        return self.name


class Photo(Timestampable, models.Model):
    ''' Gallery Photos Page '''
    title = models.CharField("Photo title", max_length=255, default="")
    description = models.TextField("Short description", blank=True, default="")
    picture = models.ImageField(upload_to='gallery_photos')
    tags = models.ManyToManyField("gallery.Tag", related_name="photos", blank=True)

    class Meta:
        ''' Custom Model metadata '''
        verbose_name_plural = "Gallery Page Photos"
        ordering = ['created_at']

    def __str__(self):
        ''' Return string data '''
        return self.title




