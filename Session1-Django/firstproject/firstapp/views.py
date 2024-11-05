from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def response_view(request):
    return HttpResponse(100)

def json_view(request):
    return JsonResponse({"hello":"world"})


def html_view(request):

    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hello</h1>
        <h1>Hello</h1>
        
    </body>
    </html>

    """)


def template_view(request):
    return render(request, "index.html")