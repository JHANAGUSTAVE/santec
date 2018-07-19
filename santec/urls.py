from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^/$', views.index, name='index'),
	url(r'^appointment/', views.appointment),
	url(r'^login/$', views._login, name='login'),
	url(r'^logout/$', views._logout, name='logout'),
	url(r'^appointment/', views.appointment, name="appointment"),

	url('ajouter_dossier/', views.ajouter_dossier, name="ajouter_dossier"),
	url('liste_dossiers/', views.liste_dossiers, name="liste_dossiers"),
	url('editer_dossier/(?P<num>[0-9]+)/$', views.editer_dossier, name="editer_dossier"),

]
