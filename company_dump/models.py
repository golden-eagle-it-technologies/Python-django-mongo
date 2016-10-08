from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
import operator, datetime

class CompanyDump(Document):
  website = StringField(blank=True, null=True)
  updated = StringField(blank=True, null=True)
  linkedin_id = StringField(blank=True, null=True)
  automatically_generated = StringField(blank=True, null=True)
  also_viewed = StringField(blank=True, null=True)
  name = StringField(blank=True, null=True)
  industry = StringField(blank=True, null=True)
  last_visited = StringField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  followers = StringField(blank=True, null=True)
  employees_on_linkedin = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  _key = StringField(blank=True, null=True)
  overview = StringField(blank=True, null=True)
  founded = StringField(blank=True, null=True)
  size = StringField(blank=True, null=True)
  type = StringField(blank=True, null=True)
  specialties = StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  last_posts_timestamps = StringField(blank=True, null=True)
  city = StringField(blank=True, null=True)
  state = StringField(blank=True, null=True)
  hq =  StringField(blank=True, null=True)
  street_1 = StringField(blank=True, null=True)
  postal = StringField(blank=True, null=True)
  country = StringField(blank=True, null=True)
  street_2 = StringField(blank=True, null=True)
  affiliated_companies = StringField(blank=True, null=True)
