from django.shortcuts import render

# Create your views here.
def testing(request):
    return render(request, 'testing.html')
def home(request):  
    return render(request, 'index.html')
