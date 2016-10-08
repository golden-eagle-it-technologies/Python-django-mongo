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
  title = StringField(blank=True, null=True)
  start = DateTimeField(blank=True, null=True)
  end = DateTimeField(blank=True, null=True)
  duration = IntField(blank=True, null=True) # store duration in number of months (Integer Format)
  location = StringField(blank=True, null=True)
  description = StringField(blank=True, null=True)
  company = ReferenceField(Company, blank=True, null=True)

  @classmethod
  def fields_list(cls):
    fields = [ f.name for f in cls._meta.fields ]
    return fields

  @classmethod
  def build_experience(cls, data):
    exp = {}
    exp_fields = cls.fields_list()
    for item in exp_fields:
      
      if item in data:
        if item == 'title':
          exp[item] = pattern.sub(' ', data[item]).strip()
        elif item in ['start', 'end']:
          if data[item] == 'Present':
            tdd = date.today()
            exp[item] = date(tdd.year, tdd.month, 1)
          elif data[item]:
            dd = data[item].split(' ')
            if dd[0].isalpha():
              month = int(MONTHS.index(str(dd[0])) + 1)
              year = int(dd[1])
            elif dd[0].isnumeric():
              month = 1
              year = int(dd[0])
            exp[item] = date(year, month, 1)
        elif item == 'company':
          try:
            uid = data['organization'][0]['unique_id']
            company = Company.objects.get(unique_id=uid)
            exp[item] = company
          except:
            exp[item] = None
        else:
          exp[item] = data[item]
      else:
        exp[item] = None

    exp['duration'] = (exp['end'] - exp['start']).days / 30 if exp['start'] and exp['end'] else None
    return cls.objects.create(**exp)

class User(Document):
  linkedin_id = StringField(blank=True, null=True)
  full_name = StringField(blank=True, null=True)
  given_name = StringField(blank=True, null=True)
  family_name = StringField(blank=True, null=True)
  url = StringField(blank=True, null=True)
  canonical_url = StringField(blank=True, null=True)
  locality = StringField(blank=True, null=True)
  last_visited = StringField(blank=True, null=True)
  num_connections = StringField(blank=True, null=True)
  summary = StringField(blank=True, null=True)
  image_url = StringField(blank=True, null=True)
  unique_id = StringField(blank=True, null=True)
  previous_urls = ListField(blank=True, null=True)
  languages = ListField(blank=True, null=True)
  experiences = ListField(ReferenceField(Experience), default=list, blank=True, null=True)
  industry = ReferenceField(Industry, blank=True, null=True)
  updated = DateTimeField(blank=True, null=True)
  last_visited = DateTimeField(blank=True, null=True)

  @classmethod
  def fields_list(cls):
    fields = [ f.name for f in cls._meta.fields ]
    return fields