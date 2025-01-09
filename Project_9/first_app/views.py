
# Create your views here.
from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# cookie ---
def set_cookie(request):
    response = render(request, 'set_cookie.html')
    response.set_cookie('name', 'rahim')
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    return response
def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def del_cookie(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response
