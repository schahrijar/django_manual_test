from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<font size='+20'><p style='color:cyan;'>Home Page</p></font>")


