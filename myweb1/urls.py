from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='Home Page'),
    path('admin/', admin.site.urls),
    path('months/', include('appmonths.urls')),
]
