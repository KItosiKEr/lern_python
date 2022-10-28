from django.shortcuts import render


def laptop(request):
    return render(request, 'laptop/laptop.html')

# Create your views here.
