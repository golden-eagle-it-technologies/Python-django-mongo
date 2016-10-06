from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import fields, Document
from datetime import datetime, date
import operator
from company.models import Company

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

class Experience(Document):
  title = fields.StringField(blank=True, null=True)
  start = fields.DateTimeField(blank=True, null=True)
  end = fields.DateTimeField(blank=True, null=True)
  duration = fields.IntField(blank=True, null=True) # store duration in number of months (Integer Format)
  location = fields.StringField(blank=True, null=True)
  description = fields.StringField(blank=True, null=True)
  organization = fields.ReferenceField(Company, blank=True, null=True)

  def save(self):
    if self.start:
      sdate = self.start.split(' ')
      if sdate[0].isalpha():
        month = int(MONTHS.index(str(sdate[0])) + 1)
        year = int(sdate[1])
      elif sdate[0].isnumeric():
        month = 1
        year = int(sdate[0])
      self.start = date(year, month, 1)

    if self.end == 'Present':
      self.end = None
    elif self.end:
      edate = self.end.split(' ')
      if edate[0].isalpha():
        month = int(MONTHS.index(str(edate[0])) + 1)
        year = int(edate[1])
      elif edate[0].isnumeric():
        month = 1
        year = int(edate[0])
      self.end = date(year, month, 1)

    if self.start and self.end:
      self.duration = (self.end - self.start).days / 30 # convert deltatime days to months
    else:
      self.duration = None

    super(Experience, self).save()
    return self
  
  @property
  def startDate(self):
    return MONTHS[self.start.month-1] + ' ' + str(self.start.year)
  


class People(Document):
  interests = fields.ListField(blank=True, null=True)
  updated = fields.StringField(blank=True, null=True)
  linkedin_id = fields.StringField(blank=True, null=True)
  organizations = fields.ListField(blank=True, null=True)
  recommendations_preview = fields.ListField(blank=True, null=True)
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
  test_scores = fields.ListField(blank=True, null=True)
  image_url = fields.StringField(blank=True, null=True)
  given_name = fields.StringField(blank=True, null=True)
  recommendations = fields.StringField(blank=True, null=True)
  url = fields.StringField(blank=True, null=True)
  skills = fields.ListField(blank=True, null=True)
  unique_id = fields.StringField(blank=True, null=True)
  publications = fields.ListField(blank=True, null=True)
  previous_urls = fields.ListField(blank=True, null=True)
  _key = fields.StringField(blank=True, null=True)
  companies = fields.ListField(fields.ReferenceField(Company), default=list, blank=True, null=True)
  experiences = fields.ListField(fields.ReferenceField(Experience), default=list, blank=True, null=True)

  @property
  def langs(self):
    try:
      temp = ', '.join(map(operator.itemgetter('name'), self.languages)) if self.languages else 'None'
    except:
      temp = None
    return temp

  @property
  def totalExperience(self):
    duration = 0
    for experience in self.experiences:
      if experience.start and experience.end:
        months = (experience.end - experience.start).days / 30
      elif experience.start and not experience.end:
        months = (datetime.now() - experience.start).days / 30
      else:
        months = 0
      duration += months
    years = duration / 12
    months = duration % 12
    if years and months:
      total = str(years) + ' year(s) ' + str(months) + ' month(s)'
    elif years:
      total = str(years) + ' year(s)'
    elif months:
      total = str(months) + ' month(s)'
    else:
      total = '0 month'

    return total


  