from django.urls import re_path
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^$', app.views.gallery, name='gallery'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    re_path(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'),

    # Auth related urls
    re_path(r'^accounts/login/$', views.LoginView.as_view(), name='login'),  # Use .as_view()
    re_path(r'^logout$', views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),  # Use .as_view() and pass next_page

    # Enable the admin
    re_path(r'^admin/', admin.site.urls),

    # Enable admin documentation
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.handler404'
