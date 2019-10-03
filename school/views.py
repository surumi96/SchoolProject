from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import date
from . import models
from .models import Book,Order,Student,Timetable
from django.contrib import messages
import sweetify


# Create your views here.
def Form(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        #studclass = request.POST.get("studclass")
        emailid = request.POST.get("email")
        #fine = request.POST.get("fine")
        password = request.POST.get("password")
        confirm_password = request.POST.get("psw")
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=emailid, password=password)
            user.save()
            return redirect('login')
    return render(request,'form.html', {})


def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("pass")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            print("user not exist")
        else:
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('studentadmin')
    return render(request, 'login.html', {})


def Academicyear(request):
    if request.method == 'POST':
        academicyearname = request.POST.get("academicyear")
        startson=request.POST.get("startson")
        endson=request.POST.get('endson')
        obj=models.Academicyear()
        obj.academicyearname=academicyearname
        obj.startson=startson
        obj.endson=endson
        obj.save()
    return render(request, 'academicyear.html',{})


def Course_view(request):
    obj1 = models.Academicyear.objects.all()
    print(obj1)
    if request.method=='POST':
        course=request.POST.get("course")
        academicyear = request.POST.get('academicyear')
        obj=models.Course()
        obj.coursename=course
        obj.academicid=models.Academicyear.objects.get(academicyearname=academicyear)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        obj.save()
        print(obj.academicid)
    return render(request, 'course.html', {"key":obj1})


def Batch(request):
    obj1 = models.Academicyear.objects.all()
    obj2=models.Course.objects.all()
    if request.method == 'POST':
        batch=request.POST.get("batch name")
        course = request.POST.get("course")
        academicyear = request.POST.get('academicyear')
        obj = models.Batch()
        obj.batchname = batch
        obj.academicid = models.Academicyear.objects.get(academicyearname=academicyear)
        obj.courseid=models.Course.objects.get(id=course)

        obj.save()
        print(obj.academicid)

    return render(request,'batch.html',{'key1':obj1,'key2':obj2})
def Admin_view(request):
    return render(request, 'admin.html', {})


def Admission(request):
    obj1 = models.Academicyear.objects.all()
    obj2 = models.Course.objects.all()
    obj3 = models.Batch.objects.all()
    if request.method=="POST":
        admissionnumber = request.POST.get("admissionnumber")
        admissionyear = request.POST.get("admissionyear")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        emailid = request.POST.get("email")
        dateofbirth = request.POST.get("dob")
        bloodgroup = request.POST.get("bloodgroup")
        phonenumber = request.POST.get("phonenumber")
        contactdetails = request.POST.get("contactdetails")
        gender = request.POST.get("gender")
        rollno = request.POST.get("rollno")
        batch = request.POST.get("batch")
        academicyear=request.POST.get("academicyear")
        course=request.POST.get("course")

        obj=models.Student()
        obj.AdmissionNumber=admissionnumber
        obj.AdmissionYear=admissionyear
        obj.FirstName=firstname
        obj.LastName=lastname
        obj.Email=emailid
        obj.DOB=dateofbirth
        obj.BloodGroup=bloodgroup
        obj.PhoneNumber=phonenumber
        obj.ContactDetails=contactdetails
        obj.Gender=gender
        obj.academicyear=models.Academicyear.objects.get(academicyearname=academicyear)
        obj.RollNo=rollno
        print('ccccccccccccccccccccccccccccccccccccccccccccccccccccc')
        print(course)
        obj.course=models.Course.objects.get(id=course)
        obj.Batch=models.Batch.objects.get(id=batch)

        obj.save()
        return redirect('admin')

    return render(request,'admission.html', {'key1':obj1,'key2':obj2,'key3':obj3})


def teacherdetails(request):
    if request.method =="POST":
        Name = request.POST.get("name")
        Designation = request.POST.get("designation")
        Education = request.POST.get("education")
        Experiance = request.POST.get("experiance")
        Subject =request.POST.get("subject")
        Gender = request.POST.get("gender")
        obj=models.Teacher()
        obj.Name=Name
        obj.Designation=Designation
        obj.Education=Education
        obj.Experiance=Experiance
        obj.Subject=Subject
        obj.Gender=Gender
        obj.save()
        return redirect('admin')
    return render(request, 'teacherdetails.html', {})


def teacherlist(request):
    obj=models.Teacher.objects.all()
    return render(request, 'teacherlist.html', {'key':obj} )

# def library(request):
#     obj = Student.objects.all()
#     return render(request,'new.html',{'key': obj})


def Studentlist(request):
    obj=Student.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        idd =request.POST.get('delete')
        ob = Student.objects.get(id=idd)
        ob.delete()
    return render(request,'new.html', {'key':obj})


def Editstudent(request, id):
    obj=Student.objects.get(id=id)
    if request.method =='POST':
        admissionnumber = request.POST.get("admissionnumber")
        obj.AdmissionNumber=admissionnumber
        admissionyear = request.POST.get("admissionyear")
        obj.AdmissionYear=admissionyear
        firstname = request.POST.get("firstname")
        obj.FirstName=firstname
        lastname = request.POST.get("lastname")
        obj.LastName=lastname
        emailid = request.POST.get("email")
        obj.Email=emailid
        dateofbirth = request.POST.get("dob")
        obj.DOB=dateofbirth
        bloodgroup = request.POST.get("bloodgroup")
        obj.BloodGroup=bloodgroup
        phonenumber = request.POST.get("phonenumber")
        obj.PhoneNumber=phonenumber
        contactdetails = request.POST.get("contactdetails")
        obj.ContactDetails=contactdetails
        gender = request.POST.get("gender")
        obj.Gender=gender
        rollno = request.POST.get("rollno")
        obj.RollNo=rollno
        batch = request.POST.get("batch")
        obj.batch=batch
        obj.save()
        return redirect('studentlist')
    return render(request,'editstudent.html',{})


def order(request):
    today=date.today()

    msg=''
    ob=Order.objects.filter(returndate=None)
    if request.method == 'POST':
        if 'issue' in request.POST:
            AdmissionNumber = request.POST.get("admissionnumber")
            BookName = request.POST.get("bookname")
            student=Student.objects.get(AdmissionNumber=AdmissionNumber)
            try:
                BookName=Book.objects.get(BookName=BookName)
                print('------------------------------------------------------------------------------------------------')
                print(BookName)
                t=Order.objects.filter(student=student, returndate=None)
                s=Order.objects.filter(returndate=None, BookName=BookName, student=student)

                if BookName.Number > 0:
                    if len(t) < 2 and len(s) == 0:
                        obj=Order()
                        obj.student=student
                        obj.BookName=BookName
                        obj.save()
                        BookName.Number -= 1
                        BookName.save()
                else:
                    msg="yes"
            except:
                msg="No"

        if 'return' in request.POST:
            admissionnumber = request.POST.get("admissionnumber")
            BookName = request.POST.get("bookname")
            student = Student.objects.get(AdmissionNumber=admissionnumber)
            BookName = Book.objects.get(BookName=BookName)
            obj = Order.objects.filter(student=student, BookName=BookName)

            for i in obj:
                i.returndate = today
                i.save()
            BookName.Number += 1
            BookName.save()
        # obj=Order.objects.filter(username=username, BookName=BookName)
    sweetify.error(request, 'no such books', persistent=':(')

    return render(request, 'vieworder.html',{'key':ob,'key1':msg})


def timetable(request):
    obj=Timetable.objects.all()
    if request.method =='POST':
        day=request.POST.method("day")
        standard=request.POST.get("standard")
        period1=request.POST.get("period1")
        period2 = request.POST.get("period2")
        period3 = request.POST.get("period3")
        period4 = request.POST.get("period4")
        period5 = request.POST.get("period5")
        period6 = request.POST.get("period6")

    return render(request,'timetable.html', {'key':obj})


def history(request):
    obj = Order.objects.exclude(returndate=None)
    return render(request, 'history.html', {'key':obj})


def edit(request,id):
    obj = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get("username")
        obj.username = username
        # studclass = request.POST.get("studclass")
        # obj.studclass = studclass
        email =request.POST.get("email")
        obj.email=email
        # fine = request.POST.get("fine")
        # obj.fine = fine
        obj.save()
        return redirect('student')
    return render(request, 'edit.html', {'key': obj})



def search(request):
    obj = Book.objects.filter(BookName= request.POST.get("bname"), Number__gt=0)
    return render(request, 'search.html', {'key': obj})



def editbook(request,id):
    obj = Book.objects.get(id=id)
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        obj.BookName = BookName
        AuthorName=request.POST.get("authorname")
        obj.AuthorName = AuthorName
        Number =request.POST.get("number")
        obj.Number =Number
        obj.save()
        return redirect('book')
    return render(request, 'editbook.html', {})


def bookform(request):
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        AuthorName = request.POST.get("authorname")
        Number = request.POST.get("number")
        print(BookName, AuthorName, Number)
        book =Book.objects.create(BookName=BookName,AuthorName=AuthorName,Number=Number)
        book.save()
        return redirect("book")
    return render(request, 'bookform.html', {})

def book(request):
    obj=Book.objects.all()
    if request.method == 'POST' and 'add' in request.POST:
        return redirect('bookform')
    if request.method == 'POST' and 'delete' in request.POST:
        idd =request.POST.get('delete')
        ob = Book.objects.get(id=idd)
        ob.delete()
    return render(request, 'book.html', {'key':obj})



def Studentadmin(request):
    return render(request, 'studentadmin.html' ,{})