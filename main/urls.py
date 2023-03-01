from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'

urlpatterns = [
    path('home', views.base, {'name': 'Home'}, name='index'),
    path('company', views.base, {'name': 'Company'}, name='index'),
    path('development', views.base, {'name': 'Development'}, name='index'),
    path('development-cpp', views.base, {'name': 'Development C++'}, name='index'),
    path('price', views.base, {'name': 'Price'}, name='index'),
    path('price-from-russia', views.base, {'name': 'Price from Russia'}, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
