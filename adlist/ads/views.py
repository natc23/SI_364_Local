# Create your views here.
from ads.models import Ad

from django.views import View
from django.views import generic
from django.shortcuts import render

from ads.util import AdlistListView, AdlistDetailView, AdlistCreateView, AdlistUpdateView, AdlistDeleteView

class AdListView(AdlistListView):
    model = Ad
    template_name = "ad_list.html"

class AdDetailView(AdlistDetailView):
    model = Ad
    template_name = "ad_detail.html"

class AdCreateView(AdlistCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ad_form.html"

class AdUpdateView(AdlistUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ad_form.html"

class AdDeleteView(AdlistDeleteView):
    model = Ad
    template_name = "ad_delete.html"
