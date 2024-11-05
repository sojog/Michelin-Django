from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def answer_view(request):
    return HttpResponse("Here is your answer")

def search_view(request):
    # http://127.0.0.1:8001/search?q=water
    print(request.GET)
    # print(request.GET["q"]) - prone to errors
    print(request.GET.get("q"))
    query = request.GET.get("q", "nothing")
    return HttpResponse(f"You are looking for {query}")

def addition_view(request):
    # http://127.0.0.1:8001/add?a=10&b=5
    a = request.GET.get("a")
    b = request.GET.get("b")
    try:
        a = int(a)
        b = int(b)
    except:
        return HttpResponse(f"a + b = impossible") 
    return HttpResponse(f"a + b = {a+b}")  


def next_value_view(request, num, num2="Default"):
    # http://127.0.0.1:8001/next/30/ # num2=Default
    # http://127.0.0.1:8001/next/20/hello/
    return HttpResponse(f"You passed the path {num} and {num2}")  