from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator

class CompanyData(Document):
  meta = {"collection": "company"}

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

  def _get_employees_count(self):
    return len(self.employees_on_linkedin) if self.employees_on_linkedin else 'None'

  employees_count = property(_get_employees_count)

class PeopleData(Document):
  meta = {"collection": "people"}

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
  experiences = StringField(blank=True, null=True)
  patents = StringField(blank=True, null=True)

  def _get_languages(self):
    try:
      return ', '.join(map(operator.itemgetter('name'), self.languages)) if self.languages else 'None'
    except:
      return 'Not Processable'

  planguages = property(_get_languages)