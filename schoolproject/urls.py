from django.urls import path
from . import views

app_name = 'schoolproject'
urlpatterns = [
	path('', views.index, name='index'),
	path('contact', views.contact, name='contact'),
	path('contactlogic', views.contactlogic, name='contactlogic'),
	path('wie', views.wie, name='wie'),
	path('aanbod', views.aanbod, name='aanbod'),

]


