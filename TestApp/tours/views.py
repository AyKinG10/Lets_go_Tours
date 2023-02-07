from django.shortcuts import render
from .models import Tours
def tours_home(request):
    tours = Tours.objects.order_by('price')
    return render(request, 'tours/tours_home.html',{'tours': tours})