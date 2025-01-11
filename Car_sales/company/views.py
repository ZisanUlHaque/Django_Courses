# company/views.py
from django.shortcuts import render, get_object_or_404
from posts.models import Post
from company.models import Company

def company_posts(request, company_slug):
    company = get_object_or_404(Company, slug=company_slug)
    posts = Post.objects.filter(company=company)
    return render(request, 'company_posts.html', {'company': company, 'posts': posts})