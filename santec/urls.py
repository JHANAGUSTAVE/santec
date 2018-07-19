from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.index, name ='index'),
	url(r'^appointment/', views.appointment),
	url(r'^login/$', views._login, name='login'),
	url(r'^logout/$', views._logout, name='logout'),
	url(r'^appointment/', views.appointment, name="appointment"),

	url(r'^ajouter_dossier', views.ajouter_dossier, name="ajouter_dossier"),
	#url(r'^ajouter_dossier', views.ajouter_dossier, name="ajouter_dossier"),
]
