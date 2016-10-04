from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
from django_mongoengine.forms.fields import DictField
# from django_mongoengine.views import ListView, DetailView
from django.views.generic.list import ListView

from people.models import People

def get_people(request, people_id=None):
  if people_id:
    rdata = {}
    people_data = { }
    people = People.objects.get(id=people_id)
    rdata['people'] = people_data
    rdata['key'] = people._key
    people_fields = People._meta.get_fields()
    for item in people_fields:
      key = item.name
      if key in ['interests', 'skills']:
        if people[key] != None:
          people_data[key] = ', '.join(people[key])
        else:
          people_data[key] = ''
      elif key == 'languages':
        people_data[key] = people.langs
      else:
        people_data[key] = people[key]

    return render(request, 'people/show.html', rdata)
  else:
    return redirect('/')


class PeopleIndexView(ListView):
  document = People
  queryset = People.objects.all()
  context_object_name = 'peoples_list'
  template_name = 'people/index.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    try:
      sort = data['sort']
    except:
      sort = 'full_name'
    try:
      name = data['search']
    except:
      name = ''
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list



class PeopleBasicListingView(ListView):
  document = People
  template_name = 'people/basic_listing.html'
  context_object_name = 'peoples_list'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    try:
      sort = data['sort']
    except:
      sort = 'full_name'
    try:
      name = data['search']
    except:
      name = ''
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

class PeopleExperienceListingView(ListView):
  document = People
  template_name = 'people/experience_listing.html'
  context_object_name = 'peoples_list'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    try:
      sort = data['sort']
    except:
      sort = 'full_name'
    try:
      name = data['search']
    except:
      name = ''
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list
