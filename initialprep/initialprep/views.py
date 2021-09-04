# new creation - self managed
# Imports 

import re
# from typing_extensions import ParamSpec
from django.http import HttpResponse, response
from django.shortcuts import render  #to use from templates



def index(request):
    # print(request.GET.get('text','default'))
    return render(request,'index.html') # with render request param is paased along with the template name <index.html>

    # return HttpResponse("This String")  - Basic
    # pass

# Params to Get request
def about(request):
    return HttpResponse("About page")

def removepunc(request):
    # pass
    print(request.GET.get('removepunc','off'))
    print(request.GET.get('text','default'))
    case = request.GET.get('removepunc','off')
    text = request.GET.get('text','default')
    if case == 'on':
        clean = extract(text)
        # cleanString = re.sub('\W+','', text)
        params = {'var': 'String', 'analyzed': clean}
        return render(request,'page.html', params)
    else:
      return HttpResponse("Use checkbox")  
    # return HttpResponse("removepunc")

def extract(text):
    cleanString = re.sub('\W+','', text)
    return cleanString


# methods are by default get can change it topost accordingly to check the error of url too long as well as to send other infos in the message body
# CSRF - Cross Site Request Forgery

