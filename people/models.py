from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

from django_mongoengine import Document, EmbeddedDocument
from django_mongoengine import fields
import operator

import datetime

class People(Document):
  interests = fields.StringField()
  updated = fields.StringField()
  linkedin_id = fields.StringField()
  organizations = fields.StringField()
  recommendations_preview = fields.StringField()
  family_name = fields.StringField()
  also_viewed = fields.StringField()
  websites = fields.StringField()
  full_name = fields.StringField()
  courses = fields.StringField()
  education = fields.StringField()
  canonical_url = fields.StringField()
  projects = fields.StringField()
  groups = fields.StringField()
  honors_awards = fields.StringField()
  certifications = fields.StringField()
  volunteering = fields.StringField()
  locality = fields.StringField()
  headline = fields.StringField()
  industry = fields.StringField()
  last_visited = fields.StringField()
  num_connections = fields.StringField()
  experience = fields.StringField()
  summary = fields.StringField()
  languages = fields.StringField()
  test_scores = fields.StringField()
  image_url = fields.StringField()
  given_name = fields.StringField()
  recommendations = fields.StringField()
  url = fields.StringField()
  skills = fields.StringField()
  unique_id = fields.StringField()
  publications = fields.StringField()
  previous_urls = fields.StringField()
  _key = fields.StringField()

  def get_absolute_url(self):
    return reverse('post', kwargs={"slug": self.id})

  def __unicode__(self):
    return self.linkedin_id

  @property
  def langs(self):
    return ', '.join(map(operator.itemgetter('name'), self.languages)) if self.languages else 'None'
