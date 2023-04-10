from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name="index"),
    path('servicios', views.servicios, name="servicios"),
    path('about', views.about, name="about"),
    path('contacto', views.contacto, name="contacto"),
    path('proyectos', views.proyectos, name="proyectos")

]