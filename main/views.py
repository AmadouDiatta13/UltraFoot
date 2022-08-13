from django.shortcuts import render
from .models import Photo, Coach, Contact, Presentation, Objectif


def home(request):
    photos = Photo.objects.all()
    coaches = Coach.objects.all()
    contacts = Contact.objects.all()
    presentations = Presentation.objects.all()
    objectifs = Objectif.objects.all()
    return render(request, 'index.html', { 'photos':photos, 'coaches':coaches, 'contacts':contacts, 'presentations': presentations, 'objectifs':objectifs})