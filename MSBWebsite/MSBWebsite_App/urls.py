from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="MSBWebsite_App"),
    path('aktywny_wyscig', views.active_race, name="active_race"),
    path('dodaj_wyscig', views.add_race, name="add_race"),
    path('zakonczone_wyscigi', views.ended_race, name="ended_race"),
]