from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
dic_months = {
    'January': "this is January in dictionary",
    'February': "this is February in dictionary",
    'March': "this is March in dictionary",
    'April': "this is April in dictionary",
    'May': "this is May in dictionary",
    'June': "this is June in dictionary",
    'July': "this is July in dictionary",
    'August': "this is August in dictionary",
    'September': "this is September in dictionary",
    'October': "this is October in dictionary",
    'November': "this is November in dictionary",
    'December': "this is December in dictionary",
}

def index(request):
    data = dic_months.keys()
    lst_items = ''
    for i in data:
        lst_items+=f"<ul><li><a href='{i}'>{i}</a></li></ul>"
    return HttpResponse('<h1>List Of Months:</h1>'+lst_items)
def dynamic_int(request,n):
    lst_keys=list(dic_months.keys())
    if n>len(lst_keys):
        HttpResponseNotFound(f"<font size='20' style='color: red;'>Page Not Found (404)<br>{n} Does Not Exist.</font>")
    choosed_key = lst_keys[n-1]
    # return HttpResponse(f"<font size='20' style='color: green;'>{n}:{choosed_key} :{dic_months[choosed_key]}</font>")
    return HttpResponseRedirect(f'/months/{choosed_key}')


def dynamic_str(request, m):

    if m in dic_months.keys():
        return HttpResponse(f"<font size='20' style='color: green;'>{m} : {dic_months.get(m)}</font>")
        # return HttpResponse(dic_months.values())

    return HttpResponseNotFound(f"<font size='20' style='color: red;'>Page Not Found (404)<br>{m} Does Not Exist.</font>")
def homepage(request):
    # redirect_data = render_to_string('appmonths/homepage.html')
    # return HttpResponse(redirect_data)
    # return HttpResponse(render_to_string('appmonths/homepage.html'))
    dic = {'name':'sara', 'code':1000}
    return render(request,'appmonths/homepage.html', context=dic)

# def months(request):
#     lst_keys = list(dic_months.keys())
#     lst_values = list(dic_months.values())
#     context={'lst_keys':lst_keys,'lst_values':lst_values}
#     return render(request,'months.html', context)
def monthspage(request):
    lst = list(dic_months.keys())
    context = {'keys':lst}
    return render(request,'appmonths/months.html', context=context)
def sum(request):

    context = {'a':20, 'b':4}

    return render(request,'appmonths/sum.html', context=context)


