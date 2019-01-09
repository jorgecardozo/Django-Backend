from django.conf.urls import url,include
from .views import _list, _detail

urlpatterns = [
    url(r'^personas/$', _list),
    url(r'^personas/(?P<id>[0-9]+)/$', _detail),
]