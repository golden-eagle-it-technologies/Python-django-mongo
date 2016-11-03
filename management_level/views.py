from django_mongoengine.views import ListView, DetailView, UpdateView
from management_level.models import ManagementLevel
from django.views.generic import UpdateView
from users.models import Designation
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

class ManagementLevelIndexView(ListView):
  document = ManagementLevel
  context_object_name = 'management_level'
  template_name = 'management_level/index.html'
  paginate_by = 4

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


class ManagementLevelDetailView(DetailView):
    document = ManagementLevel
    context_object_name = 'management_level'
    template_name = 'management_level/detail.html'
    paginate_by = 10

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

class ManagementLevelDesignationView(ListView):
  document = Designation
  context_object_name = 'designations'
  template_name = 'users/designation_management_level_listing.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'title'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      if(field=='size'):
        field = field
      else:
        field = field + '__icontains'
      object_list = self.document.objects(**{field : name}).filter(title__ne='').order_by(sort)
    else:
      object_list = self.document.objects(title__ne='').order_by(sort)
    return object_list

def get_management_level_data(request):
  managementLevel = ManagementLevel.objects.order_by('name')
  return HttpResponse(managementLevel.to_json())

@csrf_exempt
def management_level_designation_update(request):
  if request.POST:
    data = request.POST
    designation = Designation.objects.get(id=data['pk'])
    management_level = ManagementLevel.objects.get(id=data['value'])
    designation.management_level = management_level.name
    designation.save()
    
    return HttpResponse('Updated Successfully')