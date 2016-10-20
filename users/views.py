from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView
from datetime import datetime, date

from users.models import User, Experience
from companies.models import Company
from raw_data.models import CompanyData, PeopleData
from industries.models import Industry

def index(request):
  rdata = {}
  rdata['company_data'] = CompanyData.objects.count()
  rdata['people_data'] = PeopleData.objects.count()
  rdata['industries'] = Industry.objects.count()
  rdata['companies'] = Company.objects.count()
  rdata['users'] = User.objects.count()
  return render(request, 'index.html', rdata)

def get_user(request, user_id=None):
  if user_id:
    rdata = {}
    user_data = { }
    user = User.objects.get(id=user_id)
    rdata['user'] = user_data
    user_fields = User._meta.get_fields()
    for item in user_fields:
      key = item.name
      if key in ['interests', 'skills']:
        if user[key] != None:
          user_data[key] = ', '.join(user[key])
        else:
          user_data[key] = ''
      elif key == 'languages':
        user_data[key] = user.planguages
      else:
        user_data[key] = user[key]

    return render(request, 'users/show.html', rdata)
  else:
    return redirect('/')

class UserIndexView(ListView):
  document = User
  context_object_name = 'users'
  template_name = 'users/index.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(full_name__nin=[None,'']).order_by(sort)
    else:
      object_list = self.document.objects(full_name__nin=[None,'']).order_by(sort)
    return object_list

class UserBasicListingView(ListView):
  document = User
  template_name = 'users/basic_listing.html'
  context_object_name = 'users'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(full_name__nin=[None,'']).order_by(sort)
    else:
      object_list = self.document.objects(full_name__nin=[None,'']).order_by(sort)
    return object_list

class UserExperienceListingView(ListView):
  document = User
  template_name = 'users/experience_listing.html'
  context_object_name = 'users'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(full_name__nin=[None,'']).order_by(sort)
    else:
      object_list = self.document.objects(full_name__nin=[None,'']).order_by(sort)
    return object_list

class UserCurrentExperiencesView(ListView):
  document = User
  template_name = 'users/current_experience.html'
  context_object_name = 'users'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(full_name__nin=[None,'']).order_by(sort)
    else:
      object_list = self.document.objects(full_name__nin=[None,'']).order_by(sort)
    return object_list

class UserImproperDataView(ListView):
  document = User
  context_object_name = 'users'
  template_name = 'users/index.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(full_name__in=[None,'']).order_by(sort)
    else:
      object_list = self.document.objects(full_name__in=[None,'']).order_by(sort)
    return object_list
