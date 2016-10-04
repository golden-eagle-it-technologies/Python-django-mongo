from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView

from company.models import Company

class CompanyIndexView(ListView):
  document = Company
  template_name = 'company/index.html'
  context_object_name = 'companies_list'
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
      
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list


def get_company(request, company_id=None):
  if company_id:
    rdata = {}
    company_data = {}
    company = Company.objects.get(id=company_id)
    rdata['company'] = company_data
    rdata['key'] = company._key
    company_fields = Company._meta.get_fields()
    for item in company_fields:
      key = item.name
      if key == 'last_posts_timestamps':
        company_data[key] = company.lposts_timestamps
      else:
        company_data[key] = company[key]

    return render(request, 'company/show.html', rdata)
  else:
    return redirect('/')

