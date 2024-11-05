from django.shortcuts import render

# Create your views here.

def hardcoded_view(request):
    return render(request, "hardcoded.html")


def team_view(request):
    team = [
        [("Dida", "BR")], 
        [("Cafu", "BR"), 
         ("Nesta", "IT"), 
         ("Maldini", "IT"),
         ("Jankulovski", "NL")],
        [("Gattuso", "IT"), 
         ("Pirlo", "IT"), 
        ("Ambrosini", "IT")], 
        [("Seedorf", "NL"),
          ("Kaka", "BR")], 
        [("Inzaghi", "IT")]
        ]

    context = {
        'team_lines' : team
    }

    return render(request, "team.html", context)