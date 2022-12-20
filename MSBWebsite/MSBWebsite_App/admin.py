from django.contrib import admin

from .models import Route,Statistics,Ranking,Race,User,Practice
# Register your models here.

admin.site.register(Route)

admin.site.register(Statistics)

admin.site.register(Ranking)

admin.site.register(Race)

admin.site.register(User)

admin.site.register(Practice)