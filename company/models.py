from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import fields, Document, EmbeddedDocument
import operator, datetime

class Company(Document):
  website = fields.StringField()
  updated = fields.StringField()
  linkedin_id = fields.StringField()
  automatically_generated = fields.StringField()
  also_viewed = fields.StringField()
  name = fields.StringField()
  industry = fields.StringField()
  last_visited = fields.StringField()
  url = fields.StringField()
  followers = fields.StringField()
  employees_on_linkedin = fields.StringField()
  unique_id = fields.StringField()
  _key = fields.StringField()
  overview = fields.StringField()
  founded = fields.StringField()
  size = fields.StringField()
  type = fields.StringField()
  specialties = fields.StringField()
  image_url = fields.StringField()
  last_posts_timestamps = fields.StringField()
  city = fields.StringField()
  state = fields.StringField()
  hq =  fields.StringField()
  street_1 = fields.StringField()
  postal = fields.StringField()
  country = fields.StringField()
  street_2 = fields.StringField()
  affiliated_companies = fields.StringField()

  @property
  def lposts_timestamps(self):
    return ', '.join(self.last_posts_timestamps) if self.last_posts_timestamps else 'None'