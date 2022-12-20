from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import requests
import datetime


@login_required(login_url='/authentication/login')
def index(request):


    return render(request,'MSBWebsite_App/index.html')


@login_required(login_url='/authentication/login')
def active_race(request):


    return render(request,'MSBWebsite_App/active_race.html')


@login_required(login_url='/authentication/login')
def add_race(request):


    return render(request,'MSBWebsite_App/add_race.html')


@login_required(login_url='/authentication/login')
def ended_race(request):


    return render(request,'MSBWebsite_App/ended_race.html')

    