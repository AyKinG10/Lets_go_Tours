from django.shortcuts import render

def index(request):
    data = {
        'title': 'Басты бет',
    }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request,'main/about.html')
def balance(request):
    return render(request,'')
def not_found(request,exception):
    return render(request,'error_page/not_found.html')
def not_serv(request):
    return render(request, 'error_page/not_found.html')