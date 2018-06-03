
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *



urlpatterns = {
    url(r'^api/executor/$', ExecutorListView.as_view()),
    url(r'^api/executor/(?P<pk>\d+)/$', ExecutorDetailView.as_view()),
    url(r'^api/application/$', ApplicationListView.as_view()),
    url(r'^api/application/(?P<pk>\d+)/$', ApplicationDetailView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)