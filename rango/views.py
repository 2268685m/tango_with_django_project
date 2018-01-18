from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> ,<a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says Hi from the About page. <br/> ,<a href='/rango/'>Index</a>")
