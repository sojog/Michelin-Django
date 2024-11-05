"""
URL configuration for mathematics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from operations import views

## FACTORIAL for a certain value

## URL FROM PROJECT
urlpatterns = [
    path('admin/', admin.site.urls),


    path('template', views.template_view),
    path('template/<int:value>', views.template_view),
    path('template/<int:value>/<int:max>', views.template_view),
    path('<int:value>', views.multiplication_view),
    path('<int:value>/<int:max>', views.multiplication_view),
    path('query', views.query_multiplication_view),
    path('factorial/<int:number>', views.factorial_view),


    path('football/', include('football.urls')),
]
