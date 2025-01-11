from django.shortcuts import render
from posts.models import Post
from company.models import Company



def home(request, company_slug = None):
    data = Post.objects.all()
    if company_slug is not None:
        company = Company.objects.get(slug = company_slug)
        data = Post.objects.filter(company  = company)
    company = Company.objects.all()
    return render(request, 'home.html', {'data' : data, 'companies' : company})