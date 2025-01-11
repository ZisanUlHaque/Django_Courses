from django.urls import path
from posts.views import home  # Adjust this import based on where home is defined
from .views import company_posts  # Assuming company_posts is defined in company/views.py

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('company/<slug:company_slug>/', company_posts, name='company_wise_post'),  # Company posts page
]