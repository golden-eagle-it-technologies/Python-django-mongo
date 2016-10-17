from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator, re

from companies.models import Company
from industries.models import Industry

pattern = re.compile('[\W_]+', re.UNICODE)

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Experience(Document):
  company = StringField(blank=True, null=True)
  description = StringField(blank=True, null=True)
  duration = StringField(blank=True, null=True)
  present = BooleanField(blank=True, null=True)
  end = StringField(blank=True, null=True)
  end_month = IntField(blank=True, null=True)
  end_year = IntField(blank=True, null=True)
  location = StringField(blank=True, null=True)
  start = StringField(blank=True, null=True)
  start_month = IntField(blank=True, null=True)
  start_year = IntField(blank=True, null=True)
  title = StringField(blank=True, null=True)

  meta = {"collection": "new_experience"}


class User(Document):
  current_industry = StringField(blank=True, null=True)
  canonical_url = StringField(blank=True, null=True)
  vanity_url = BooleanField(blank=True, null=True)
  experiences = ListField(ReferenceField(Experience), default=list, blank=True, null=True)
  family_name = StringField(blank=True, null=True)
  full_name = StringField(blank=True, null=True)
  given_name = StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  industry = ReferenceField(Industry, blank=True, null=True)
  languages = ListField(blank=True, null=True)
  last_visited = StringField(blank=True, null=True)
  linkedin_id = StringField(blank=True, null=True)
  locality = StringField(blank=True, null=True)
  num_connections = StringField(blank=True, null=True)
  summary = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  updated = DateTimeField(blank=True, null=True)
  url = StringField(blank=True, null=True)

  meta = {"collection": "new_people"}
