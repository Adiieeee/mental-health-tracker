from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306244980',
        'name': 'Muhammad Adiansyah',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
