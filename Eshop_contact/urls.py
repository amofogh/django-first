from django.urls import path, include
from .views import contact_us_view, about_us

app_name = 'contact'
urlpatterns = [
    path('contact-us', contact_us_view, name='contact_us'),
    path('about-us', about_us, name='about_us'),
]
