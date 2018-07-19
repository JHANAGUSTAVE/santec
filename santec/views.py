from django.http import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout


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

		user = authenticate(request, username = username, password = password)

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

	data = {'heading': 'Nouveau dossier'}
	return render(request, "admin/ajouter_dossier.html", data)



