from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^enter_trip$', views.enter_trip),
    url(r'^add_trip$', views.add_trip),
    # url(r'^view_trip/(?P<id>\d+)$',TemplateView.as_view(template_name='view_trip.html'),name="view_trip")
    url(r'^view_trip/(?P<id>\d+)$', views.view_trip),
]