from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.namein, name='namein'),
]
#url(r'^$', views.post_list),
