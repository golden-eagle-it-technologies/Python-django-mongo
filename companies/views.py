from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView
from companies.models import Company
from industries.models import Industry

class CompanyIndexView(ListView):
  document = Company
  template_name = 'companies/index.html'
  context_object_name = 'companies'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'name'
    name = data['search'] if 'search' in data else ''
    
    if name != '':
      field = data['filter']
      if(field!='is_system'):
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).order_by(sort)
      else:
        name = True if name == '1' else False
        object_list = self.document.objects(is_system=name).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

class CompanyImproperDataView(ListView):
  document = Company
  template_name = 'companies/index.html'
  context_object_name = 'companies'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'name'
    name = data['search'] if 'search' in data else ''
    
    if name != '':
      field = data['filter']
      if(field!='is_system'):
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).order_by(sort)
      else:
        name = True if name == '1' else False
        object_list = self.document.objects(is_system=name).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

def get_company(request, company_id=None):
  if company_id:
    rdata = {}
    company = Company.objects.get(id=company_id)
    rdata['company'] = company
    return render(request, 'companies/show.html', rdata)
  else:
    return redirect('/')

def get_industries(request):
  industries = Industry.objects.order_by('name')
  return HttpResponse(industries.to_json())