from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import math


def multiplication_view(request, value, max=10):
    print(type(value))
    # try:
    #     value = int(value)    
    # except:
    #     return HttpResponse(f"You sent a non numerical value")
    
    response_string = ""
    for i in range(1, max+1):
        response_string += f"{i}x{value} = {i * value} <br>"

    return HttpResponse(f"{response_string}")


def query_multiplication_view(request):
    num = request.GET.get("num")
    try:
        value = int(num)
        return multiplication_view(request, value)
    except:
        return HttpResponse(f"Here you will have your response")
    
def template_view(request, value = 3, max=10):
    response_string = ""
    collection = [f"{i} x {value} = { i * value }" for i in range(1, max+1)]
    context = {
        "liquid": response_string,
        "collection" : collection,
        "value":value,
    }
    return render(request, "multiplication.html", context)

def factorial_view(request, number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    context = {
        "number":number,
        "factorial": math.factorial(number)
    }
    return render(request, "factorial.html", context)