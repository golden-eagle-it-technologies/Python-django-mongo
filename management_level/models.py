from __future__ import unicode_literals
from django.db import models
from django_mongoengine.fields import *
from django_mongoengine import Document

class ManagementLevel(Document):

    meta = {"collection": "management_level"}

    name = StringField(blank=True, null=True)
    keyword = ListField(default=map, blank=True, null=True)

    def __unicode__(self):
        return self.name
