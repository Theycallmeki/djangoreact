from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('', home),  # Root URL shows this view
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]
