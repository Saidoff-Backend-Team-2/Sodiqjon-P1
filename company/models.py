from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media
from common.utils import phone_number_validator
from phonenumber_field.modelfields import PhoneNumberField


class Banner(models.Model):
    """Homepage"""
    title = models.CharField(_('title'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255)
    bg_image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banner')


class AboutUs(models.Model):
    """About Us Page"""
    desc = models.TextField(_('description'))
    video = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.id}-{self.desc}"

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')


class AboutUsGallery(models.Model):
    """Gallery"""
    image = models.OneToOneField(Media, blank=True, null=True, on_delete=models.SET_NULL)
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, related_name='about_us')

    def __str__(self):
        return f"{self.about_us}-{self.image.file.url}"

    class Meta:
        verbose_name = _('About Us Gallery')
        verbose_name_plural = _('About Us Galleries')


class Contact(models.Model):
    """Contact Page"""
    address = models.TextField(_('address'))
    phone_number = PhoneNumberField(_('phone number'))
    work_time = models.CharField(_('work time'), max_length=255)

    def __str__(self):
        return f"{self.pk}-{self.address}"

    class Meta:
        verbose_name = _('Contacts')
        verbose_name_plural = _('Contacts')


class SocialMedia(models.Model):
    """Social Media Icons"""
    link = models.URLField(_('link'))
    icon = models.CharField(_('icon'), max_length=255, help_text=_('write icon code'))

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Medias')


class ContactWithUs(models.Model):
    """Feedback Section"""
    full_name = models.CharField(_('full name'), max_length=255)
    phone_number = PhoneNumberField(_('phone number'))
    subject = models.CharField(_('subject'), max_length=255)
    message = models.TextField(_('message'))

    class Meta:
        verbose_name = _('Contact With Us')
        verbose_name_plural = _('Contact With Us')
