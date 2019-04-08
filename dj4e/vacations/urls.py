from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.MainView.as_view(), name='vacations'),
    path('main/create/', views.TripCreate.as_view(), name='trip_create'),
    path('main/<int:pk>/update/', views.TripUpdate.as_view(), name='trip_update'),
    path('main/<int:pk>/delete/', views.TripDelete.as_view(), name='trip_delete'),
    path('lookup/', views.LocationView.as_view(), name='location_list'),
    path('lookup/create/', views.LocationCreate.as_view(), name='location_create'),
    path('lookup/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
    path('lookup/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
]
