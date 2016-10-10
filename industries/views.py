from django.shortcuts import render
from django.db import models
from django.core.urlresolvers import reverse
from django_mongoengine import Document
from django_mongoengine.fields import *
from datetime import datetime, date
import operator, re
from companies.models import Company
from industries.models import Industry
from users.models import User

class IndustryIndexView(ListView):
  document = Industry
  context_object_name = 'industries_list'
  template_name = 'industry/index.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    try:
      sort = data['sort']
    except:
      sort = 'name'
    try:
      name = data['search']
    except:
      name = ''
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      
      industries = self.document.objects(**{field : name}).order_by(sort)
    else:
      industries = self.document.objects.order_by(sort)
    object_list = []

    for industry in industries:
      all_users = User.objects.filter(industry=industry)
      all_companies = Company.objects.filter(industry=industry)
      data = {'user_count':len(all_users),'company_count':len(all_companies),'industry':industry}
      object_list.append(data)

    return object_list

