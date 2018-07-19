from django.http import *
from django.shortcuts import render, HttpResponse, redirect


def index(request):
	return render(request, "index.html")


def services(request):
	return render(request, "services.html")


def departments(request):
	return render(request, "departments.html")


def departments_single(request):
	return render(request, "departments-single.html")


def blog(request):
	return render(request, "blog.html")


def blog_single(request):
	return render(request, "blog-single.html")


def doctors(request):
	return render(request, "doctors.html")


def doctors_single(request):
	return render(request, "doctors-single.html")


def appointment(request):
	return render(request, "appointment.html")


def contact(request):
	return render(request, "contact.html")
