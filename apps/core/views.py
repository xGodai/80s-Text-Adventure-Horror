from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the 80s Text Adventure Horror Game!")
