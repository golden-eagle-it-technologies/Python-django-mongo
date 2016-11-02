from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator, re

from companies.models import Company
from industries.models import Industry
from management_level.models import ManagementLevel

pattern = re.compile('[\W_]+', re.UNICODE)

current_date = date.today()

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
class Department(Document):
  meta = {"collection": "department"}
  name = StringField(blank=True, null=True)


  def __unicode__(self):
    return self.title

class Experience(Document):
  meta = {"collection": "new_experience"}

  company = ReferenceField(Company, blank=True, null=True)
  department = ReferenceField(Department, blank=True, null=True)
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

  @property
  def pend_month(self):
    return 'Present' if current_date.year == self.end_year and current_date.month == self.end_month else self.end_month

  @property
  def pend_year(self):
    return 'Present' if current_date.year == self.end_year else self.end_year

  @property
  def user_name(self):
    try:
      return User.objects.get(experiences__in=[self.id])
    except:
      return {}


class User(Document):
  meta = {"collection": "new_people"}

  current_industry = ReferenceField(Industry, blank=True, null=True)
  department = ReferenceField(Department, blank=True, null=True)
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

  @property
  def planguages(self):
    try:
      return (', '.join(map(str, self.languages))).title() if self.languages else 'None'
    except:
      return 'Not Processable'

  @property
  def latest_experience(self):
    return self.experiences and self.experiences[0] or {}

  @property
  def current_experience(self):
    if(self.experiences):
      count = len(self.experiences)

      ctx = {}

      last_exp = self.experiences[0]
      first_exp = self.experiences[count-1]
      years = ((last_exp.end_year or current_date.year) - first_exp.start_year) if first_exp.start_year else None
      months = ((last_exp.end_month or current_date.month) - first_exp.start_month) if first_exp.start_year and first_exp.start_month else None
      if(months < 0):
        years -= 1
        months += 12

      ctx['duration_month'] = months
      ctx['duration_year'] = years
      ctx['start'] = first_exp.start
      ctx['end'] = last_exp.end

      d_months = 0
      d_years = 0
      for exp in self.experiences:
          if exp.duration_month:
            d_months += exp.duration_month
          if exp.duration_year:
            d_years += exp.duration_year

      if d_months > 12:
        d_years += d_months/12
        d_months = d_months%12

      ctx['d_months'] = d_months
      ctx['d_years'] = ctx['duration_year'] if ctx['duration_year'] < d_years else d_years

      return ctx
    else:
      return None

  @property
  def user_email(self):
    try:
      return UserEmail.objects.get(people_id=self.id)
    except:
      return None

  @property
  def management_level(self):
      try:
          return ManagementLevel.objects.get(keyword__icontains=self.latest_experience.title)
      except:
          return None

class UserEmail(Document):
  meta = {"collection": "user_email"}

  reason = StringField(blank=True, null=True)
  found = BooleanField(blank=True, null=True)
  correctness = IntField(blank=True, null=True)
  company_id = ReferenceField(Company, blank=True, null=True)
  people_id = ReferenceField(User, blank=True, null=True)
  email = StringField(blank=True, null=True)
  confidence = StringField(blank=True, null=True)
  name = StringField(blank=True, null=True)
  surname = StringField(blank=True, null=True)
  domain = StringField(blank=True, null=True)

  def __unicode__(self):
    return self.email