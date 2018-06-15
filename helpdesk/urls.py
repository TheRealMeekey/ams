
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *



urlpatterns = {
    url(r'^executor/$', ExecutorListView.as_view()),
    url(r'^ticket_list/$', TicketListView.as_view()),
    url(r'^ticket/(?P<pk>\d+)/$', TicketDetailView.as_view()),
    url(r'^my_ticket/$', MyTicketView.as_view()),
    url(r'^ticket_history/$', HistoryTicketView.as_view()),
    url(r'^ticket_new/$', TicketCreateView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)