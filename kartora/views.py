from django.http import HttpResponse

from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, Vishal! Your Django setup works perfectly.")
