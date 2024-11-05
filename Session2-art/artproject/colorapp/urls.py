from django.urls import path
from .views import form_view, answer_view 

urlpatterns = [ 
    path("form", form_view),
    path('answer', answer_view),
]