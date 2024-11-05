
from django.urls import path
from .views import *

## CHESS APP URL
urlpatterns = [
    path('form', size_form_view),
    path('board', simple_chess_board_view, name="board_url"),
]
