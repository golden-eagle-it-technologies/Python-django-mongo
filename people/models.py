from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import fields, Document
import operator, datetime
from company.models import Company

class People(Document):
  interests = fields.ListField(blank=True, null=True)
  updated = fields.StringField(blank=True, null=True)
  linkedin_id = fields.StringField(blank=True, null=True)
  organizations = fields.ListField(blank=True, null=True)
  recommendations_preview = fields.StringField(blank=True, null=True)
  family_name = fields.StringField(blank=True, null=True)
  also_viewed = fields.ListField(blank=True, null=True)
  websites = fields.ListField(blank=True, null=True)
  full_name = fields.StringField(blank=True, null=True)
  courses = fields.ListField(blank=True, null=True)
  education = fields.ListField(blank=True, null=True)
  canonical_url = fields.StringField(blank=True, null=True)
  projects = fields.ListField(blank=True, null=True)
  groups = fields.ListField(blank=True, null=True)
  honors_awards = fields.ListField(blank=True, null=True)
  certifications = fields.ListField(blank=True, null=True)
  volunteering = fields.ListField(blank=True, null=True)
  locality = fields.StringField(blank=True, null=True)
  headline = fields.StringField(blank=True, null=True)
  industry = fields.StringField(blank=True, null=True)
  last_visited = fields.StringField(blank=True, null=True)
  num_connections = fields.StringField(blank=True, null=True)
  experience = fields.ListField(blank=True, null=True)
  summary = fields.StringField(blank=True, null=True)
  languages = fields.ListField(blank=True, null=True)
  test_scores = fields.StringField(blank=True, null=True)
  image_url = fields.StringField(blank=True, null=True)
  given_name = fields.StringField(blank=True, null=True)
  recommendations = fields.ListField(blank=True, null=True)
  url = fields.StringField(blank=True, null=True)
  skills = fields.ListField(blank=True, null=True)
  unique_id = fields.StringField(blank=True, null=True)
  publications = fields.ListField(blank=True, null=True)
  previous_urls = fields.StringField(blank=True, null=True)
  _key = fields.StringField(blank=True, null=True)
  companies = fields.ListField(fields.ReferenceField(Company), default=list, blank=True, null=True)

  @property
  def langs(self):
    try:
      temp = ', '.join(map(operator.itemgetter('name'), self.languages)) if self.languages else 'None'
    except:
      temp = None
    return temp
