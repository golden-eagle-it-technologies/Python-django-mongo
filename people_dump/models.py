from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator

class PeopleDump(Document):
  interests = ListField(blank=True, null=True)
  updated = StringField(blank=True, null=True)
  linkedin_id = StringField(blank=True, null=True)
  organizations = ListField(blank=True, null=True)
  recommendations_preview = ListField(blank=True, null=True)
  family_name = StringField(blank=True, null=True)
  also_viewed = ListField(blank=True, null=True)
  websites = ListField(blank=True, null=True)
  full_name = StringField(blank=True, null=True)
  courses = ListField(blank=True, null=True)
  education = ListField(blank=True, null=True)
  canonical_url = StringField(blank=True, null=True)
  projects = ListField(blank=True, null=True)
  groups = ListField(blank=True, null=True)
  honors_awards = ListField(blank=True, null=True)
  certifications = ListField(blank=True, null=True)
  volunteering = ListField(blank=True, null=True)
  locality = StringField(blank=True, null=True)
  headline = StringField(blank=True, null=True)
  industry = StringField(blank=True, null=True)
  last_visited = StringField(blank=True, null=True)
  num_connections = StringField(blank=True, null=True)
  experience = ListField(blank=True, null=True)
  summary = StringField(blank=True, null=True)
  languages = ListField(blank=True, null=True)
  test_scores = ListField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  given_name = StringField(blank=True, null=True)
  recommendations = StringField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  skills = ListField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  publications = ListField(blank=True, null=True)
  previous_urls = ListField(blank=True, null=True)
  _key = StringField(blank=True, null=True)

  meta = {"collection": "people"}
