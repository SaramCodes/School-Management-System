from django.conf.urls import url
from .views import (
    user_creation_view,
    login_view,
    user_view,
    user_detail,
    user_delete,
    user_list,
    user_update_view,
    change_password,
    steacher_update_view,
    logout_view)


urlpatterns = [
    url(r'^register/$', user_creation_view, name='user_creation_view'),
    url(r'^(?P<id>[\w-]+)/edit$', user_update_view, name='user_update_view'),
    url(r'^(?P<id>[\w-]+)/detail$', user_detail, name='user_detail'),
    url(r'^(?P<id>[\w-]+)/delete$', user_delete, name='user_delete'),
    url(r'^(?P<id>[\w-]+)/info_update$', steacher_update_view, name='steacher_update'),
    url(r'^login/$', login_view, name='login_view'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^$', user_view, name='user_view'),
    url(r'^password/$', change_password, name='change_password'),
    url(r'^logout/$', logout_view, name='logout_view'),


]
