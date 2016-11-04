from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import ListView, DetailView
from datetime import datetime, date

from users.models import *
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
      if(field=='updated' or field== 'last_visited'):
        dateObject = datetime.strptime(name, "%Y-%m-%d").date()
        field_lte = field + '__lte'
        field_gte = field + '__gte'
        object_list = self.document.objects(**{field_gte:datetime.combine(dateObject, datetime.min.time()),field_lte:datetime.combine(dateObject, datetime.max.time())}).filter(is_proper=True).order_by(sort)
      else:
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).filter(is_proper=True).order_by(sort)
    else:
      object_list = self.document.objects(is_proper=True).order_by(sort)
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
      if(field=='updated' or field== 'last_visited'):
        dateObject = datetime.strptime(name, "%Y-%m-%d").date()
        field_lte = field + '__lte'
        field_gte = field + '__gte'
        object_list = self.document.objects(**{field_gte:datetime.combine(dateObject, datetime.min.time()),field_lte:datetime.combine(dateObject, datetime.max.time())}).filter(is_proper=True).order_by(sort)
      else:
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).filter(is_proper=True).order_by(sort)
    else:
      object_list = self.document.objects(is_proper=True).order_by(sort)
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
      if(field=='updated' or field== 'last_visited'):
        dateObject = datetime.strptime(name, "%Y-%m-%d").date()
        field_lte = field + '__lte'
        field_gte = field + '__gte'
        object_list = self.document.objects(**{field_gte:datetime.combine(dateObject, datetime.min.time()),field_lte:datetime.combine(dateObject, datetime.max.time())}).filter(is_proper=True).order_by(sort)
      else:
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).filter(is_proper=True).order_by(sort)
    else:
      object_list = self.document.objects(is_proper=True).order_by(sort)
    return object_list

class UserCurrentExperiencesView(ListView):
  document = User
  template_name = 'users/current_experience.html'
  context_object_name = 'users'
  paginate_by = 25

  @staticmethod
  def filters(data):
    ctx = {'is_proper':True}
    if data.get('search',False):
      field = data['filter']
      if field in ['updated','last_visited'] :
        search_date = datetime.strptime(data.get('search'), "%Y-%m-%d").date()
        ctx.update({field + '__lte':search_date})
      else:
        ctx.update({field + '__icontains':data.get('search')})
    return ctx

  def get_queryset(self):
    data = self.request.GET
    filters = self.filters(data)
    object_list = self.document.objects(**filters).order_by(data.get('sort','full_name'))
    return object_list

class UserImproperDataView(ListView):
  document = User
  context_object_name = 'users'
  template_name = 'users/improper_data_listing.html'
  paginate_by = 50

  def get_queryset(self):
    data = self.request.GET
    
    sort = data['sort'] if 'sort' in data else 'full_name'
    name = data['search'] if 'search' in data else ''

    if (name != ''):
      field = data['filter']
      if(field=='updated' or field== 'last_visited'):
        dateObject = datetime.strptime(name, "%Y-%m-%d").date()
        field_lte = field + '__lte'
        field_gte = field + '__gte'
        object_list = self.document.objects(**{field_gte:datetime.combine(dateObject, datetime.min.time()),field_lte:datetime.combine(dateObject, datetime.max.time())}).filter(is_proper=False).order_by(sort)
      else:
        field = field + '__icontains'
        object_list = self.document.objects(**{field : name}).filter(is_proper=False).order_by(sort)
    else:
      object_list = self.document.objects(is_proper=False).order_by(sort)
    return object_list

class UserDesignationView(ListView):
  document = Designation
  context_object_name = 'designations'
  template_name = 'users/designation_department_listing.html'
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

class UserDesignation2View(ListView):
  document = Designation
  context_object_name = 'designations'
  template_name = 'users/designation_department2_listing.html'
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

class UserDepartmentView(ListView):
  document = Department
  context_object_name = 'departments'
  template_name = 'users/department_listing.html'
  paginate_by = 50

@csrf_exempt
def department_create(request):
  if request.POST:
    data = request.POST
    Department.objects.create(name=data['department_name'])
    return HttpResponseRedirect('/users/departments-listing/')

@csrf_exempt
def department_update(request):
  if request.POST:
    data = request.POST
    if data['name'] == 'department_name':
      department = Department.objects.get(id=data['pk'])
      department.name = data['value']
      department.save()

    else:
      designation = Designation.objects.get(id=data['pk'])
      department = Department.objects.get(id=data['value'])
      
      if data['name'] == 'department1':
        designation.department = department.name
        designation.departmentUpdate()
        
      elif data['name'] == 'department2':
        designation.department2 = department.name
        designation.department2Update()
      
    return HttpResponse('Updated Successfully') 

def get_departments(request):
  departments = Department.objects.order_by('name')
  return HttpResponse(departments.to_json())
