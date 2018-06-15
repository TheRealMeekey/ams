
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *



urlpatterns = {
    # url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^auth/', CustomAuthToken.as_view()),
    url(r'^profile/$', ProfileView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)