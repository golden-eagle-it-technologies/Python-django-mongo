from django.conf.urls import include, url

from django_mongoengine import mongo_admin

from companies.views import *
from users.views import *
from industries.views import *
from raw_data.views import *
from management_level.views import *

urlpatterns = [
  url(r'^$', index, name="index"),
  
  url(r'^users/listing/$', UserIndexView.as_view(), name="users_index"),
  url(r'^users/basic-listing/$', UserBasicListingView.as_view(), name="users_basic"),
  url(r'^users/experience-listing/$', UserExperienceListingView.as_view(), name="users_experience"),
  url(r'^users/current-experience-listing/$', UserCurrentExperiencesView.as_view(), name="users_current_experience"),
  url(r'^users/designation-department-listing/$', UserDesignationView.as_view(), name="users_designation_department"),
  url(r'^users/designation-department2-listing/$', UserDesignation2View.as_view(), name="users_designation_department2"),
  url(r'^users/improper-listing/$', UserImproperDataView.as_view(), name="users_improper_data"),
  url(r'^users/detail/(?P<user_id>\w+)$', get_user, name="user_detail"),
  url(r'^users/department/update/$', department_update, name="department_update"),
  url(r'^users/get/departments/$', get_departments, name="get_departments"),
  url(r'^users/departments-listing/$', UserDepartmentView.as_view(), name="users_departments_listing"),
  url(r'^users/departments/create/$', department_create, name="department_create"),

  url(r'^companies/listing/$', CompanyIndexView.as_view(), name="company_index"),
  url(r'^companies/detail/(?P<company_id>\w+)$', get_company, name="company_detail"),
  url(r'^companies/improper-listing/$', CompanyImproperDataView.as_view(), name="company_improper_data"),
  
  url(r'^industries/listing/$', IndustryIndexView.as_view(), name="industry_index"),
  # url(r'^industries/detail/(?P<industry_id>\w+)$', get_industry, name="industry_detail"),
  url(r'^industries/get-all-industries/$', get_industries, name="list_industries"),
  
  url(r'^raw-data/users/listing/$', PeopleDataIndexView.as_view(), name="people_data_index"),
  url(r'^raw-data/companies/listing/$', CompanyDataIndexView.as_view(), name="company_data_index"),
  url(r'^raw-data/users/detail/(?P<people_id>\w+)$', get_people_data, name="people_data_detail"),
  url(r'^raw-data/companies/detail/(?P<company_id>\w+)$', get_company_data, name="company_data_detail"),
  
  url(r'^management_level/listing$', ManagementLevelIndexView.as_view(), name="management_level_index"),
  url(r'^management_level/detail/(?P<pk>\w+)$', ManagementLevelDetailView.as_view(), name="management_level_detail"),
  url(r'^management-level/designation-listing/$', ManagementLevelDesignationView.as_view(), name="management_level_designation_listing"),
  url(r'^management-level/get-management-level/$', get_management_level_data, name="management_level_json"),
  url(r'^management-level/designation-update/$', management_level_designation_update, name="management_level_designation_update"),
]
