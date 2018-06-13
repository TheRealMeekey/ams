
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *



urlpatterns = {
    url(r'^executor/$', ExecutorListView.as_view()),
    url(r'^application_list/$', ApplicationListView.as_view()),
    url(r'^application/(?P<pk>\d+)/$', ApplicationDetailView.as_view()),
    url(r'^my_application/$', MyApplicationView.as_view()),
    url(r'^history/$', HistoryApplicationView.as_view()),
    url(r'^application_new/$', ApplicationCreateView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)