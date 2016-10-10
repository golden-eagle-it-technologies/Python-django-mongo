from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
from django_mongoengine.forms.fields import DictField
from django.views.generic.list import ListView
import datetime
from users.models import User,Experience

def get_user(request, user_id=None):
  if user_id:
    rdata = {}
    user_data = { }
    user = User.objects.get(id=user_id)
    rdata['user'] = user_data
    rdata['key'] = user._key
    user_fields = User._meta.get_fields()
    for item in user_fields:
      key = item.name
      if key in ['interests', 'skills']:
        if user[key] != None:
          user_data[key] = ', '.join(user[key])
        else:
          user_data[key] = ''
      elif key == 'languages':
        user_data[key] = user.langs
      else:
        user_data[key] = user[key]

    return render(request, 'user/show.html', rdata)
  else:
    return redirect('/')

class UserIndexView(ListView):
  document = User
  queryset = User.objects.all()
  context_object_name = 'users_list'
  template_name = 'user/index.html'
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

class UserBasicListingView(ListView):
  document = User
  template_name = 'user/basic_listing.html'
  context_object_name = 'users_list'
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


class UserExperienceListingView(ListView):
  document = User
  template_name = 'user/experience_listing.html'
  context_object_name = 'users_list'
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


class UserCurrentExperiencesView(ListView):
  document = User
  template_name = 'user/current_experience.html'
  context_object_name = 'users_list'
  paginate_by = 50

  def get_queryset(self):
    exps = Experience.objects(end=None)
    # data = self.request.GET
    
    # try:
    #   sort = data['sort']
    # except:
    #   sort = 'full_name'
    # try:
    #   name = data['search']
    # except:
    #   name = ''
    # if (name != ''):
    #   field = data['filter']
    #   field = field + '__icontains'
    #   users = self.document.objects(experiences__in=exps,**{field : name}).order_by(sort)
    # else:
    #   users = self.document.objects(experiences__in=exps,).order_by(sort)
    users = self.document.objects(experiences__in=exps)
    user_array = []
    mindate = datetime.datetime(datetime.MINYEAR, 1, 1)
    for user in users:
      user.experiences = sorted(user.experiences, key=lambda x: x.start or mindate, reverse=True)
      user.exp = user.experiences[0]
      if user.exp.organization:
        user.c_industry = user.exp.organization.industry
      else:
        user.c_industry = 'Not Found'
      if user.exp.start is not None:
        user_array.append(user)
    return user_array