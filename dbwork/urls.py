from django.conf.urls import include, url

from django_mongoengine import mongo_admin

urlpatterns = [
  url(r'^$', UserIndexView.as_view(), name="user_index"),
  url(r'^user-basic-list/$', UserBasicListingView.as_view(), name="user_basic_listing"),
  url(r'^user-experience-list/$', UserExperienceListingView.as_view(), name="user_experience_listing"),
  url(r'^user-detail/(?P<user_id>\w+)$', get_user),
  url(r'^company-list/$', CompanyIndexView.as_view(), name="company_index"),
  url(r'^company-detail/(?P<company_id>\w+)$', get_company),
  url(r'^user-current-experiences/$', UserCurrentExperiencesView.as_view(), name="current_experience_of_user"),
  url(r'^industries/$', IndustryIndexView.as_view(), name="count_of_user_and_company_by_industry"),
]
