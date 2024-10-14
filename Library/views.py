from django.shortcuts import render
from Library.models import Student
from Library.models import Course
from Library.models import Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'firstname': 'Hazim',
        'greeting' : 1, 
    }
    return render (request,"index.html",context)

def dbstudent(request):
    mystudent = Student.objects.all().values()
    context={
        'mystudent' : mystudent,
    }
    return render (request,"dbstudent.html",context) 

def view(request):
    context={
        'name' : 'Hazmi Hazim'
    }
    return render (request,"view.html",context)

def book(request):
    return render (request,"book.html") 

def borrow(request):
    return render (request,"borrow.html") 

def course(request):
    mycourse=Course.objects.all().values()
    if request.method == 'POST':
        c_code = request.POST['code']
        c_description = request.POST['desc']
        data=Course(code=c_code, description=c_description)
        data.save()
        dict = {
            'message' : 'Data Save',
            'mycourse': mycourse
        }
    else:
        dict = {
            'message' : '',
            'mycourse': mycourse
        }
    return render (request,"course.html",dict)

def mentor(request):
    mendatab= Mentor.objects.all().values()
    if request.method == 'POST':
        x1 = request.POST['id']
        x2 = request.POST['name']
        x3 = request.POST['room']
        data=Mentor(menid=x1, menname=x2,menroomno=x3)
        data.save()
        dict = {
            'message': 'Data Save'
        }
    else:
        dict = {
            'message': ''
        }
    dict = {
        'mendatabase' : mendatab
    }
    return render (request,"mentor.html",dict)

def update_course(request,code):
    data =Course.objects.get(code=code)
    dict ={
        'data': data
    }
    return render(request,"update_course.html",dict)

def save_update_course(request,code):
    c_desc=request.POST['desc']
    mycourse=Course.objects.get(code=code)
    mycourse.description = c_desc
    mycourse.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data =Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None

        context = {
            'data': data
        }

        return render(request, "search_course.html", context)
