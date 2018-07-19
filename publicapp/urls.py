from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='public'),
	url(r'^services/$', views.services, name='services'),
	url(r'^departments/$', views.departments, name='departments'),
	url(r'^departments/single/$', views.departments_single, name='departments-single'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^blog/single/$', views.blog_single, name='blog-single'),
	url(r'^doctors/$', views.doctors, name='doctors'),
	url(r'^doctors/single/$', views.doctors_single, name='doctors-single'),
	url(r'^appointment/$', views.appointment, name='appointment'),
	url(r'^contact/$', views.contact, name='contact'),

]
