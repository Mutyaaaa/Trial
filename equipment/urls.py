from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'equipment'

urlpatterns = [
	path('', views.equipment, name='bio-app-equipment'),
	url(r'^(?P<Category_id>[0-9]+)/$', views.detail, name='bio-app-detail'),
	url(r'^(?P<Category_id>[0-9]+)/(?P<Item_id>[0-9]+)/$', views.item, name='bio-app-item'),
]
