from django.conf.urls import url
from .views import (
    OrderAPIView,
    OrderCreateAPIView,
    OrderDetailAPIView,
    OrderUpdateAPIView,
    OrderDeleteAPIView
)


urlpatterns = [
    url(r'^$', OrderAPIView.as_view()),
    url(r'^create/$', OrderCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', OrderDetailAPIView.as_view()),
    url(r'^(?P<pk>\d+)/update/$', OrderUpdateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', OrderDeleteAPIView.as_view()),
]


# /ap/status/ -> List
# /ap/status/create -> Create
# /ap/status/id -> Detail
# /ap/status/id/update -> Update
# /ap/status/id/delete -> Delete
