# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel

from .managers import Mp3Manager


class Mp3(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel):
	file = models.FileField(upload_to='nump3/mp3s/%Y/%m/%d')
	img = models.ImageField(upload_to='nump3/thumbs/%Y/%m/%d', blank=True)

	objects = Mp3Manager()

	class Meta:
		verbose_name = _('Mp3')
		verbose_name_plural = _('Mp3s')
		ordering = ('-created',)

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('nump3s:detail', kwargs={'slug': self.slug})