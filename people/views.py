from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView

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
  context_object_name = 'peoples_list'
  template_name = 'people/index.html'
  paginate_by = 50


class PeopleBasicListingView(ListView):
  document = People
  template_name = 'people/basic_listing.html'
  context_object_name = 'peoples_list'
  paginate_by = 50


class PeopleExperienceListingView(ListView):
  document = People
  template_name = 'people/experience_listing.html'
  context_object_name = 'peoples_list'
  paginate_by = 50
