from __future__ import unicode_literals
from background_task import background
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import fields, Document, EmbeddedDocument
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

  def get_absolute_url(self):
    return reverse('post', kwargs={"slug": self.id})

  def __unicode__(self):
    return self.linkedin_id

  @property
  def langs(self):
    return ', '.join(map(operator.itemgetter('name'), self.languages)) if self.languages else 'None'

  @classmethod
  def update_people_companies(clr):
    peoples = clr.objects.all()
    for people in peoples:
      if people.experience and not people.companies:
        companies_list = []
        for experience in people.experience:
          try:
            for org in experience['organization']:
              if org['unique_id']:
                companies_list.append(str(org['unique_id']))
          except Exception as e:
            e
        try:
          people.companies = companies_list
          people.save()
          print people
        except Exception as e:
          e
    return 'success'
