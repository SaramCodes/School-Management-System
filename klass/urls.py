from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    klasses_list_view,
    klasses_detail_view,
    klasses_create_view,
    klasses_delete_view,
    klasses_update_view,
)

urlpatterns =[
    # This is Klasses pages
    url(r'^list/$', klasses_list_view, name='klasses_list_view'),
    url(r'^create/$', klasses_create_view, name='klasses_create_view'),
    url(r'^(?P<id>[\w-]+)/$', klasses_detail_view, name='klasses_detail_view'),
    url(r'^(?P<id>[\w-]+)/delete$', klasses_delete_view, name='klasses_delete_view'),
    url(r'^(?P<id>[\w-]+)/edit$', klasses_update_view, name='klasses_update_view'),
    #End klasses pages

]
