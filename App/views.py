from django.shortcuts import render

def index(req):
    return render(req,'index.html')

def Contact(req):
    return render(req,'Contact.html')