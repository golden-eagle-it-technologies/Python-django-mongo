from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView
from raw_data.models import CompanyData, PeopleData

class CompanyDataIndexView(ListView):
  document = CompanyData
  template_name = 'raw_data/companies/index.html'
  context_object_name = 'companies'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else '_id'
    name = data['search'] if 'search' in data else ''
    
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

def get_company_data(request, company_id=None):
  if company_id:
    rdata = {}
    company = CompanyData.objects.get(id=company_id)
    rdata['key'] = company._key
    rdata['company'] = company
    return render(request, 'raw_data/companies/show.html', rdata)
  else:
    return redirect('/')

class PeopleDataIndexView(ListView):
  document = PeopleData
  template_name = 'raw_data/peoples/index.html'
  context_object_name = 'peoples'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else '_id'
    name = data['search'] if 'search' in data else ''
    
    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

def get_people_data(request, people_id=None):
  if people_id:
    rdata = {}
    people = PeopleData.objects.get(id=people_id)
    rdata['key'] = people._key
    people.interests = ', '.join(people.interests) if people.interests != None else ''
    people.skills = ', '.join(people.skills) if people.skills != None else ''
    rdata['people'] = people
    return render(request, 'raw_data/peoples/show.html', rdata)
  else:
    return redirect('/')