from django.http import *
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db import transaction
import sys


# Create your views here.
def appointment(request):
	return render(request, "appointment.html", {'nom': test})


# Create your views here.
def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")

	data = {'heading': 'Dashboard'}
	return render(request, "admin/layout.html", data)


def _login(request):
	if request.method == "POST":

		username = request.POST["uname"]
		password = request.POST["psw"]

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/")
		else:
			return render(request, "admin/login2.html")
	else:
		return render(request, "admin/login2.html")


def _logout(request):
	logout(request)
	return HttpResponseRedirect("/login/")


def ajouter_dossier(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")

	data = {'heading': 'Nouveau dossier', "form_action": "/ajouter_dossier/"}

	if request.method == "POST":
		try:
			prenom = request.POST["prenom"]
			nom = request.POST["nom"]
			sexe = request.POST["sexe"]
			age = request.POST["age"]

			departement = request.POST["departement"]
			ville = request.POST["ville"]
			rue = request.POST["adresse"]
			tel = request.POST["tel"]

			profession = request.POST["profession"]
			religion = request.POST["religion"]
			groupe_sanguin = request.POST["gsanguin"]
			allergie = request.POST["allergie"]

			diagnostique = request.POST["diagnostic"]

			address = Adresse()
			address.departement = departement
			address.ville = ville
			address.rue = rue
			address.save()

			personne = Personne()
			personne.nom = nom
			personne.prenom = prenom
			personne.telephone = tel
			personne.id_adresse = address
			personne.save()

			patient = Patient()
			patient.id_personne = personne
			patient.age = age
			patient.sexe = sexe
			patient.profession = profession
			patient.religion = religion
			patient.groupe_sanguin = groupe_sanguin
			patient.allergie_connu = allergie
			patient.save()

			dossier = Dossier()
			dossier.diagnostique = diagnostique
			dossier.id_patient = patient
			dossier.save()

		except Exception as ex:
			transaction.rollback()
			data['error'] = ex
			return render(request, "admin/ajouter_dossier.html", data)

		else:
			transaction.commit()
			return HttpResponseRedirect("/liste_dossiers/")

	return render(request, "admin/ajouter_dossier.html", data)


def liste_dossiers(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")

	data = {'heading': 'Liste des dossiers', "dossiers": Dossier.objects.all()}
	return render(request, "admin/liste_dossiers.html", data)


"""
Je sais! c completement con de le faire comme ca, mais il fallait que j'aille dormir.
"""


def editer_dossier(request, num=0):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")

	data = {'heading': 'Nouveau dossier'}
	dossier = get_object_or_404(Dossier, pk=num)

	data["form_action"] = "/editer_dossier/" + str(dossier.pk) + '/'

	if request.method == "POST":
		try:

			prenom = request.POST["prenom"]
			nom = request.POST["nom"]
			sexe = request.POST["sexe"]
			age = request.POST["age"]

			departement = request.POST["departement"]
			ville = request.POST["ville"]
			rue = request.POST["adresse"]
			tel = request.POST["tel"]

			profession = request.POST["profession"]
			religion = request.POST["religion"]
			groupe_sanguin = request.POST["gsanguin"]
			allergie = request.POST["allergie"]

			diagnostique = request.POST["diagnostic"]

			address = dossier.id_patient.id_personne.id_adresse
			address.departement = departement
			address.ville = ville
			address.rue = rue
			address.save()

			personne = dossier.id_patient.id_personne
			personne.nom = nom
			personne.prenom = prenom
			personne.telephone = tel
			personne.id_adresse = address
			personne.save()

			patient = dossier.id_patient
			patient.id_personne = personne
			patient.age = age
			patient.sexe = sexe
			patient.profession = profession
			patient.religion = religion
			patient.groupe_sanguin = groupe_sanguin
			patient.allergie_connu = allergie
			patient.save()

			dossier.diagnostique = diagnostique
			dossier.id_patient = patient
			dossier.save()

		except Exception as ex:
			transaction.rollback()
			data['error'] = ex
			return render(request, "admin/ajouter_dossier.html", data)

		else:
			transaction.commit()
			return HttpResponseRedirect("/liste_dossiers/")

	data["dossier"] = dossier

	return render(request, "admin/ajouter_dossier.html", data)
