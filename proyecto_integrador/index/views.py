from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.db.models import Q
import datetime


# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def servicios(request):
    return render(request, 'index/services.html')

def about(request):
    return render(request, 'index/about.html')

def contacto(request):
    return render(request, 'index/contact.html')


def proyectos(request):
    return render(request, 'index/projects.html')