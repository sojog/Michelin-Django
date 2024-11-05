from django.shortcuts import render
from .forms import SizeForm
# Create your views here.










def simple_chess_board_view(request):

    received_form = SizeForm(request.POST)
    if received_form.is_valid():
        print("The form is valid")
    else:
        print("The form is NOOOOT valid")
        print(received_form.errors)

    print(request.POST)
    N  = request.POST.get("size")
    try:
        N = int(N)
    except:
        N = 8
    context = {
        'error': received_form.errors,
        'N' : N,
        'range_N': range(N)
    }
    return render(request, "chess.html", context)

def size_form_view(request):
    # Object of type SizeForm
    size_form = SizeForm()
    context = {
        'form' : size_form
    }
    return render(request, "size_form.html", context)