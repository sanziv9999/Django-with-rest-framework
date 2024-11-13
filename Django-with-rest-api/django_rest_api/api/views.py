from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tours, TourDetails
from .forms import TourForm

class TourListView(ListView):
    model = Tours
    template_name = 'tour_list.html'
    context_object_name = 'tours'  

class TourCreateView(CreateView):
    model = Tours
    form_class = TourForm
    template_name = 'tour_form.html'
    success_url = '/tour/'
    

class TourUpdateView(UpdateView):
    model = Tours
    form_class = TourForm
    template_name = 'tour_form.html'
    success_url = '/tour/'

class TourDeleteView(DeleteView):
    model = Tours
    template_name = 'tour_confirm_delete.html'
    success_url = '/tour/'
