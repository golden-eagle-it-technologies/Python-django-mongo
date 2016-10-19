from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView
from industries.models import Industry

class IndustryIndexView(ListView):
  document = Industry
  context_object_name = 'industries'
  template_name = 'industries/index.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).order_by(sort)
    else:
      object_list = self.document.objects.order_by(sort)
    return object_list

