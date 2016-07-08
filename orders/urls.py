from django.conf.urls import url, include
from rest_framework import routers

from orders import views
from orders.api import OrderViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)


urlpatterns = [
    url(r'^list/$', views.list, name='list_order'),
    url(r'^(?P<order_id>.*)/change/$', views.change, name='change_order'),
    url(r'^change/$', views.change, name='change_order'),

    # Wire up our API using automatic URL routing.
    url(r'^', include(router.urls)),
]
