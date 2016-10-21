from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator, re

from industries.models import Industry

class Company(Document):
  meta = {"collection": "new_company"}

  also_viewed = ListField(blank=True, null=True)
  automatically_generated = BooleanField(blank=True, null=True)
  city = StringField(blank=True, null=True)
  country = StringField(blank=True, null=True)
  followers = StringField(blank=True, null=True)
  hq =  StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  industry = ReferenceField(Industry, blank=True, null=True)
  last_visited = DateTimeField(blank=True, null=True)
  linkedin_id = StringField(blank=True, null=True)
  name = StringField(blank=True, null=True)
  overview = StringField(blank=True, null=True)
  postal = StringField(blank=True, null=True)
  state = StringField(blank=True, null=True)
  street_1 = StringField(blank=True, null=True)
  street_2 = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  updated = DateTimeField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  vanity_url = BooleanField(blank=True, null=True)
  website = StringField(blank=True, null=True)
  is_system = BooleanField(blank=True, null=True,default=True)

  def __unicode__(self):
    return self.name

  @property
  def users_count(self):
    from users.models import Experience
    return Experience.objects(company=self.id).count()

  # @property
  # def linkedin_users_count(self):
  #   from raw_data.models import CompanyData
  #   try:
  #     return CompanyData.objects.get(id=self.id).employees_on_linkedin.count()
  #   except:
  #     return 0