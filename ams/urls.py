from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helpdesk/', include('helpdesk.urls')), # Add this line
    url(r'^account/', include('account.urls')),
]
