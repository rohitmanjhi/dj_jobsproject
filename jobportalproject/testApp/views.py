from django.shortcuts import render

# Create your views here.
def hydjobs(request):
    return render(request,"testApp/hyd.html")

def index(request):
    return render(request,"testApp/index.html")
