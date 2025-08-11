from django.shortcuts import render
from .models import product
# Create your views here.
def store(request):
    product = product.objects.all().filter(is_available=True)
    context = {'products':product}
    return render(request , 'store/store.html', context)