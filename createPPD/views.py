from django.shortcuts import render

# Create your views here.
def createPPD(request):
    return render(request, 'createPPD.html')