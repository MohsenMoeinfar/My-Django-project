from django.shortcuts import render
from .models import *

def show_books(request):
    books=Book.objects.all().order_by('-id')
    context={
        'books':books
    }
    return render (request, 'swbooks/index.html' , context)
def Add_book(request):
    if request.method == "GET":
        return render (request , 'swbooks/form.html')
    elif request.method == "POST" :
        data= request.POST
    Book.objects.create(bookname = data["bookname"], author = data["author"],your_name = data["your_name"],your_lastname = data["your_lastname"],your_university = data["your_university"],your_college = data["your_college"],tel_id = data["tel_id"],detail = data["detail"],you_are=data["you_are"])
    return render(request , 'swbooks/finish.html' )

def welcome(request):

    return render(request,'swbooks/welcome.html')