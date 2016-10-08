from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator, re

from industries.models import Industry

class Company(Document):
  linkedin_id = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  name = StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  website = StringField(blank=True, null=True)
  followers = StringField(blank=True, null=True)
  hq =  StringField(blank=True, null=True)
  street_1 = StringField(blank=True, null=True)
  street_2 = StringField(blank=True, null=True)
  city = StringField(blank=True, null=True)
  state = StringField(blank=True, null=True)
  postal = StringField(blank=True, null=True)
  country = StringField(blank=True, null=True)
  industry = ReferenceField(Industry, blank=True, null=True)
  overview = StringField(blank=True, null=True)
  also_viewed = ListField(blank=True, null=True)
  automatically_generated = BooleanField(blank=True, null=True)
  updated = DateTimeField(blank=True, null=True)
  last_visited = DateTimeField(blank=True, null=True)

  @classmethod
  def fields_list(cls):
    fields = [ f.name for f in cls._meta.fields ]
    return fields
