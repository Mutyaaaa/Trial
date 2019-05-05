from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'consumables'

urlpatterns = [
	path('', views.consumables, name='bio-app-consumables'),
]