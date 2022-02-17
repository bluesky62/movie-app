from ast import Num, Try
from calendar import c
from dataclasses import dataclass
import email
from email import message
import re
from typing import Any
from unicodedata import name
from urllib.request import DataHandler
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from contact_page.models import ContactPage

#from contact.models import Contact
from .form import usersform
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail
#from contact.models import Contact




def home(request):
    send_mail(
        'Subject here',
        'here is the message.',
        'akasingale62@gmail.com',
        ['akashingale62@gmail.com'],
        fail_silently=False
    )
    newsdata=News.objects.all()
    data={
        'newsdata':newsdata
    }
    return render(request, "index.html", data)

def newsDetails(request):
    if request.method == "GET":
        newsdata=News.objects.all()
        #newsdata = request.GET.get('news')
        data = {
            'newsdata':newsdata
            }
        return render(request, "newsDetails.html", data)



def about(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "about.html", {'output': output})


def Services(request):
    #service_data = Service.objects.get()
    # paginator = Paginator(service_data, 2)
    # page_number = request.GET.get('page')
    # service_data_final = paginator.get_page(page_number)
    if request.method=="GET":
        st = request.GET.get('Service')
        if st != None:
            service_data = Service.objects.filter(service_title__icontains=st)

        data = {
            'service_data':st
                }
        return render(request, "Services.html", data)
            
    return render(request, "Services.html", DataHandler)


def portfolio(request):
    return render(request, "portfolio.html")


def Team(request):
    return render(request, "team.html")


def evenodd(request):
    c = ''
    data = {}
    if request.method == "POST":
        if request.POST.get('num1')=='':
            return render(request, "evenodd.html", {'error':True})

        n = eval(request.POST.get('num1'))
        if n % 2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
        data = {
            'n': n,
            'c': c
        }

    return render(request, "evenodd.html", data)


def submitform(request):
    try:

        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            Num = n1 + n2 + n3
            data = {
                'n1': n1,
                'n2': n2,
                'n3': n3,
                'output': Num
            }
        return HttpResponse(Num)

    except:
        pass

    return HttpResponse(request, submitform)


def calculator(request):
    c = ''
    data = {}
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2

            data = {
                'n1': n1,
                'n2': n2,
                 'c': c

            }

    except:
        c = "invalid opr ...."

    return render(request, "calculator.html", data)


def contact(request):
    return render(request, "contact.html")




def saveEnquiry(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        n = ContactPage(name=name, email=email, subject=subject, message=message)
        n.save()

    return render(request, "contact.html")
    
        





def useform(request):
    Num = 0
    fn = usersform()
    data = {'form': fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            Num = n1 + n2 + n3
            data = {
                'form': fn,
                'n1': n1,
                'n2': n2,
                'n3': n3,
                'output': Num
            }

            url = "/about/?output={}".format(Num)

            return redirect(url)

    except:
        pass

    return render(request, "useform.html", data)


def marksheet(request):
    c=''
    data={}

    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t = s1 + s2 + s3 + s4 + s5
        per = t * 100 / 500
        if per >= 70:

            c ="Distinction"
        elif per>=60:

            c="First Class"
        elif per>=50:

            c = "Second Class"
        elif per>=35:
            c = "Third Class"
        data = {
            's1':s1,
            's2':s2,
            's3':s3,
            's4':s4,
            's5':s5,
            't': t,
            'per':per,
            'c':c
        }
        return render(request, "marksheet.html", data)


    
    return render(request, "marksheet.html", data)