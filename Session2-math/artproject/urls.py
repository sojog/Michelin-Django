
## URL FROM APPLICATION

from django.urls import path
from django.http import HttpResponse
from .views import hardcoded_view, team_view


urlpatterns = [ 
    path('test', lambda r:HttpResponse("ok") ),
    path('hardcoded', hardcoded_view),
    path('team', team_view)
]