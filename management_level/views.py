from django_mongoengine.views import ListView, DetailView, UpdateView
from management_level.models import ManagementLevel
from django.views.generic import UpdateView


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
