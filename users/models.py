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

current_date = date.today()

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Experience(Document):
  meta = {"collection": "new_experience"}

  # company = StringField(blank=True, null=True)
  description = StringField(blank=True, null=True)
  duration_month = IntField(blank=True, null=True)
  duration_year = IntField(blank=True, null=True)
  present = BooleanField(blank=True, null=True)
  end = StringField(blank=True, null=True)
  end_month = IntField(blank=True, null=True)
  end_year = IntField(blank=True, null=True)
  location = StringField(blank=True, null=True)
  start = StringField(blank=True, null=True)
  start_month = IntField(blank=True, null=True)
  start_year = IntField(blank=True, null=True)
  title = StringField(blank=True, null=True)
  organization = StringField(blank=True, null=True)
  company_unique_id = StringField(blank=True, null=True)
  company_name = StringField(blank=True, null=True)


  def __unicode__(self):
    return self.title

  def _get_end_month(self):
    return 'Present' if current_date.year == self.end_year and current_date.month == self.end_month else self.end_month

  pend_month = property(_get_end_month)

  def _get_end_year(self):
    return 'Present' if current_date.year == self.end_year else self.end_year

  pend_year = property(_get_end_year)

  def _get_company_industry(self):
    try:
      compobj = Company.objects.get(unique_id=self.company_unique_id)
      return compobj.industry
    except:
      return 'None'

  pcompany_industry = property(_get_company_industry)


class User(Document):
  meta = {"collection": "new_people"}

  current_industry = StringField(blank=True, null=True)
  canonical_url = StringField(blank=True, null=True)
  vanity_url = BooleanField(blank=True, null=True)
  experiences = ListField(ReferenceField(Experience), default=list, blank=True, null=True)
  family_name = StringField(blank=True, null=True)
  full_name = StringField(blank=True, null=True)
  given_name = StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  industry = StringField(blank=True, null=True)
  languages = ListField(blank=True, null=True)
  last_visited = DateTimeField(blank=True, null=True)
  linkedin_id = StringField(blank=True, null=True)
  locality = StringField(blank=True, null=True)
  num_connections = StringField(blank=True, null=True)
  summary = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  updated = DateTimeField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  headline = StringField(blank=True, null=True)

  def __unicode__(self):
    return self.full_name

  def _get_languages(self):
    try:
      return (', '.join(map(str, self.languages))).title() if self.languages else 'None'
    except:
      return 'Not Processable'

  planguages = property(_get_languages)

  def _get_current_experience(self):
    if(self.experiences):
      count = len(self.experiences)
      last_exp = self.experiences[0]
      first_exp = self.experiences[count-1]
      years = (current_date.year - first_exp.start_year) if first_exp.start_year else None
      months = (current_date.month - first_exp.start_month) if first_exp.start_year and first_exp.start_month else None
      if(months > 12):
        years -= 1
        months += 12

      last_exp['duration_month'] = months
      last_exp['duration_year'] = years
      last_exp['start'] = first_exp.start
      return last_exp
    else:
      return None

  pcurrent_experience = property(_get_current_experience)
