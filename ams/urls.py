from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/helpdesk/', include('helpdesk.urls')), # Add this line
    url(r'^api/account/', include('account.urls')),
]
