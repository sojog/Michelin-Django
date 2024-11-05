from django.shortcuts import render
from .forms import PasswordGeneratorForm
from .models import PasswordModel
# Create your views here.
import random
import string
from django.contrib.auth.decorators import login_required

def password_list_view(request):
    password_list = PasswordModel.objects.all()
    context = {
        'passwords' : password_list
    }
    return render(request, "list.html", context)


@login_required
def password_details_view(request, pk):
    password = PasswordModel.objects.filter(id=pk).first()
    context = { 
        'password' : password
    }
    return render(request, "details.html", context)


## THIS IS MY BUSINESS LOGIC
def next_password(length, with_upper, with_numbers, with_special):
    choices = string.ascii_lowercase
    if with_upper:
        choices += string.ascii_uppercase
    if with_numbers:
        choices += string.digits
    if with_special:
        choices += string.punctuation
    print("Needs to choose from", choices)
    return "".join(random.choices(choices, k=length))


def password_view(request):
    if request.method == "POST":
        ## this is for validation - with values received
        received_form = PasswordGeneratorForm(request.POST)
        if received_form.is_valid():
            size = received_form.cleaned_data["password_size"]
            print("size from received_form.cleaned_data", size, type(size))

            has_upper = received_form.cleaned_data["has_uppercase"]
            print("has_upper", has_upper, type(has_upper))

            has_no = received_form.cleaned_data["has_numbers"]

            has_special = received_form.cleaned_data["has_special_ch"]
            generated_password = next_password(size, has_upper, has_no, has_special)

            pass_obj = PasswordModel.objects.create(content=generated_password)
            print(pass_obj)

            context = {
                'password':generated_password,
                'form': PasswordGeneratorForm()
            }
        return render(request, "password.html", context)
    
    ## This is for template filling - to be filled out 
    injected_form = PasswordGeneratorForm()
    context = {
        'form': injected_form
    }
    return render(request, "password.html", context)
    

  