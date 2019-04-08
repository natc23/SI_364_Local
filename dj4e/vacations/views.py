from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from vacations.models import Trip, Location
from vacations.forms import LocationForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Location.objects.all().count();
        al = Trip.objects.all();

        ctx = { 'location_count': mc, 'trip_list': al };
        return render(request, 'vacations/trip_list.html', ctx)

class LocationView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Location.objects.all();
        ctx = { 'location_list': ml };
        return render(request, 'vacations/location_list.html', ctx)

class LocationCreate(LoginRequiredMixin, View):
    template = 'vacations/location_form.html'
    success_url = reverse_lazy('vacations')
    def get(self, request) :
        form = LocationForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = LocationForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        location = form.save()
        return redirect(self.success_url)

class LocationUpdate(LoginRequiredMixin, View):
    model = Location
    success_url = reverse_lazy('vacations')
    template = 'vacations/location_form.html'
    def get(self, request, pk) :
        location = get_object_or_404(self.model, pk=pk)
        form = LocationForm(instance=location)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        location = get_object_or_404(self.model, pk=pk)
        form = LocationForm(request.POST, instance = location)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('vacations')
    template = 'vacations/location_confirm_delete.html'

    def get(self, request, pk) :
        location = get_object_or_404(self.model, pk=pk)
        form = LocationForm(instance=location)
        ctx = { 'location': location }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        location = get_object_or_404(self.model, pk=pk)
        location.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class TripCreate(LoginRequiredMixin,CreateView):
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('vacations')

class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('vacations')

class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    fields = '__all__'
    success_url = reverse_lazy('vacations')
