from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns=[
    url(r'^$', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)