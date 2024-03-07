from django.urls import path

from . import views
urlpatterns=[

    path('home', views.homepage, name="homepage"),
    path('sum', views.sum, name="sum"),
    path('monthspage', views.monthspage, name="monthspage"),

    path('<int:n>', views.dynamic_int, name="months-int"),
    path('<str:m>', views.dynamic_str, name="months"),
    path('', views.index, name="index"),

]