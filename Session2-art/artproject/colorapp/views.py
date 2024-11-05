from django.shortcuts import render

# Create your views here.

def form_view(request):
    context = {}
    return render(request, "colorform.html", context)

def answer_view(request):
    context = { }
    
    received_color = request.GET.get("color")
    red = request.GET.get("red")
    green = request.GET.get("green")
    blue = request.GET.get("blue")

    if received_color:
        context['color'] = received_color
        
    if red and green and blue:
        context['red']  = red
        context['green'] = green
        context['blue'] = blue   

    return render(request, 'coloranswer.html', context)