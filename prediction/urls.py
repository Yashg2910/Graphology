from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^predict/', views.simple_upload, name='predict'),
    url(r'^export/', views.export, name="export"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)