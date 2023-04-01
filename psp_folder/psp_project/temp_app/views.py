from django.shortcuts import render

# Create your views here.


def temporary(request):
    return render(request, 'temp_app/temporary.html')
