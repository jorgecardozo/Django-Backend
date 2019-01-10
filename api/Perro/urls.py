from django.conf.urls import url,include
from .views import _listP, _detailP

urlpatterns = [
    url(r'^perro/$', _listP),
    url(r'^perro/(?P<id>[0-9]+)/$', _detailP),
]