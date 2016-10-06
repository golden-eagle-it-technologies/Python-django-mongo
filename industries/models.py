from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator

class Industry(Document):
  name = StringField(blank=True, null=True)

  def __unicode__(self):
    return self.name
