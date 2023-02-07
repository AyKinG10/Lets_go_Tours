from django.shortcuts import render

def index(request):
    data = {
        'title': 'Басты бет',
    }
    return render(request, 'main/index.html',data)

def about(request):
    return render(request,'main/about.html')
def balance(request):
    return render(request,'')