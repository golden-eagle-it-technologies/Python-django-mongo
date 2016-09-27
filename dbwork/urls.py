from django.conf.urls import include, url

from people.views import *

from company.views import *

from django_mongoengine import mongo_admin

urlpatterns = [
  url(r'^$', PeopleIndexView.as_view(), name="people_index"),
  url(r'^people-basic-list/$', PeopleBasicListingView.as_view(), name="people_basic_listing"),
  url(r'^people-experience-list/$', PeopleExperienceListingView.as_view(), name="people_experience_listing"),
  url(r'^people-detail/(?P<people_id>\w+)$', get_people),
  url(r'^company-list/$', CompanyIndexView.as_view(), name="company_index"),
  url(r'^company-detail/(?P<company_id>\w+)$', get_company),
  # url(r'^admin/', include(mongo_admin.site.urls)),
]
