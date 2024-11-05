

from django.urls import path
from .views import password_view, password_list_view, password_details_view

## App URL
urlpatterns = [
    path('pass', password_view),
    path('list', password_list_view),
    path('details/<int:pk>', password_details_view, name="details_url"),
]