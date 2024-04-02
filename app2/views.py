from django.shortcuts import render

# Create your views here.
def lap(request):
    return render(request,'lap.html')
