from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import date
from . import models
from .models import Book, Order, Student, Timetable, Category, Transport, Assign, Busdetails, Busstop, Busroute, \
    Feecategory
from django.contrib import messages
from datetime import datetime, timedelta


# Create your views here.
def Form(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        # studclass = request.POST.get("studclass")
        emailid = request.POST.get("email")
        # fine = request.POST.get("fine")
        password = request.POST.get("password")
        confirm_password = request.POST.get("psw")
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=emailid, password=password)
            user.save()
            return redirect('login')
    return render(request, 'form.html', {})


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
        startson = request.POST.get("startson")
        endson = request.POST.get('endson')
        obj = models.Academicyear()
        obj.academicyearname = academicyearname
        obj.startson = startson
        obj.endson = endson
        obj.save()
    return render(request, 'academicyear.html', {})


def Course_view(request):
    obj1 = models.Academicyear.objects.all()
    print(obj1)
    if request.method == 'POST':
        course = request.POST.get("course")
        academicyear = request.POST.get('academicyear')
        obj = models.Course()
        obj.coursename = course
        obj.academicid = models.Academicyear.objects.get(academicyearname=academicyear)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        obj.save()
        print(obj.academicid)
    return render(request, 'course.html', {"key": obj1})


def Batch(request):
    obj1 = models.Academicyear.objects.all()
    obj2 = models.Course.objects.all()
    if request.method == 'POST':
        batch = request.POST.get("batch name")
        course = request.POST.get("course")
        academicyear = request.POST.get('academicyear')
        obj = models.Batch()
        obj.batchname = batch
        obj.academicid = models.Academicyear.objects.get(academicyearname=academicyear)
        obj.courseid = models.Course.objects.get(id=course)

        obj.save()
        print(obj.academicid)

    return render(request, 'batch.html', {'key1': obj1, 'key2': obj2})


def Admin_view(request):
    return render(request, 'admin.html', {})


def Admission(request):
    obj1 = models.Academicyear.objects.all()
    obj2 = models.Course.objects.all()
    obj3 = models.Batch.objects.all()
    if request.method == "POST":
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
        academicyear = request.POST.get("academicyear")
        course = request.POST.get("course")

        obj = models.Student()
        obj.AdmissionNumber = admissionnumber
        obj.AdmissionYear = admissionyear
        obj.FirstName = firstname
        obj.LastName = lastname
        obj.Email = emailid
        obj.DOB = dateofbirth
        obj.BloodGroup = bloodgroup
        obj.PhoneNumber = phonenumber
        obj.ContactDetails = contactdetails
        obj.Gender = gender
        obj.academicyear = models.Academicyear.objects.get(academicyearname=academicyear)
        obj.RollNo = rollno
        print('ccccccccccccccccccccccccccccccccccccccccccccccccccccc')
        print(course)
        obj.course = models.Course.objects.get(id=course)
        obj.Batch = models.Batch.objects.get(id=batch)

        obj.save()
        return redirect('admin')

    return render(request, 'admission.html', {'key1': obj1, 'key2': obj2, 'key3': obj3})


def teacherdetails(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Designation = request.POST.get("designation")
        Education = request.POST.get("education")
        Experiance = request.POST.get("experiance")
        Subject = request.POST.get("subject")
        Gender = request.POST.get("gender")
        obj = models.Teacher()
        obj.Name = Name
        obj.Designation = Designation
        obj.Education = Education
        obj.Experiance = Experiance
        obj.Subject = Subject
        obj.Gender = Gender
        obj.save()
        return redirect('admin')
    return render(request, 'teacherdetails.html', {})


def teacherlist(request):
    obj = models.Teacher.objects.all()
    return render(request, 'teacherlist.html', {'key': obj})


# def library(request):
#     obj = Student.objects.all()
#     return render(request,'new.html',{'key': obj})


def Studentlist(request):
    obj = Student.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        ob = Student.objects.get(id=idd)
        ob.delete()
    return render(request, 'new.html', {'key': obj})


def Editstudent(request, id):
    obj = Student.objects.get(id=id)
    if request.method == 'POST':
        admissionnumber = request.POST.get("admissionnumber")
        obj.AdmissionNumber = admissionnumber
        admissionyear = request.POST.get("admissionyear")
        obj.AdmissionYear = admissionyear
        firstname = request.POST.get("firstname")
        obj.FirstName = firstname
        lastname = request.POST.get("lastname")
        obj.LastName = lastname
        emailid = request.POST.get("email")
        obj.Email = emailid
        dateofbirth = request.POST.get("dob")
        obj.DOB = dateofbirth
        bloodgroup = request.POST.get("bloodgroup")
        obj.BloodGroup = bloodgroup
        phonenumber = request.POST.get("phonenumber")
        obj.PhoneNumber = phonenumber
        contactdetails = request.POST.get("contactdetails")
        obj.ContactDetails = contactdetails
        gender = request.POST.get("gender")
        obj.Gender = gender
        rollno = request.POST.get("rollno")
        obj.RollNo = rollno
        batch = request.POST.get("batch")
        obj.batch = batch
        obj.save()
        return redirect('studentlist')
    return render(request, 'editstudent.html', {})


def order(request):
    today = date.today()

    msg = ''
    ob = Order.objects.filter(returndate=None)
    if request.method == 'POST':
        if 'issue' in request.POST:
            AdmissionNumber = request.POST.get("admissionnumber")
            BookName = request.POST.get("bookname")
            student = Student.objects.get(AdmissionNumber=AdmissionNumber)
            try:
                BookName = Book.objects.get(BookName=BookName)
                print(
                    '------------------------------------------------------------------------------------------------')
                print(BookName)
                t = Order.objects.filter(student=student, returndate=None)
                s = Order.objects.filter(returndate=None, BookName=BookName, student=student)

                if BookName.Number > 0:
                    if len(t) < 2 and len(s) == 0:
                        obj = Order()
                        obj.student = student
                        obj.BookName = BookName
                        obj.save()
                        BookName.Number -= 1
                        BookName.save()
                else:
                    msg = "yes"
            except:
                msg = "No"

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

    return render(request, 'vieworder.html', {'key': ob, 'key1': msg})


def timetable(request):
    obj = Timetable.objects.all()
    if request.method == 'POST':
        day = request.POST.method("day")
        standard = request.POST.get("standard")
        period1 = request.POST.get("period1")
        period2 = request.POST.get("period2")
        period3 = request.POST.get("period3")
        period4 = request.POST.get("period4")
        period5 = request.POST.get("period5")
        period6 = request.POST.get("period6")

    return render(request, 'timetable.html', {'key': obj})


def history(request):
    obj = Order.objects.exclude(returndate=None)
    return render(request, 'history.html', {'key': obj})


def edit(request, id):
    obj = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get("username")
        obj.username = username
        # studclass = request.POST.get("studclass")
        # obj.studclass = studclass
        email = request.POST.get("email")
        obj.email = email
        # fine = request.POST.get("fine")
        # obj.fine = fine
        obj.save()
        return redirect('student')
    return render(request, 'edit.html', {'key': obj})


def search(request):
    obj = Book.objects.filter(BookName=request.POST.get("bname"), Number__gt=0)
    return render(request, 'search.html', {'key': obj})


def editbook(request, id):
    obj = Book.objects.get(id=id)
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        obj.BookName = BookName
        AuthorName = request.POST.get("authorname")
        obj.AuthorName = AuthorName
        Number = request.POST.get("number")
        obj.Number = Number
        obj.save()
        return redirect('book')
    return render(request, 'editbook.html', {})


def bookform(request):
    if request.method == 'POST':
        BookName = request.POST.get("bookname")
        AuthorName = request.POST.get("authorname")
        Number = request.POST.get("number")
        print(BookName, AuthorName, Number)
        book = Book.objects.create(BookName=BookName, AuthorName=AuthorName, Number=Number)
        book.save()
        return redirect("book")
    return render(request, 'bookform.html', {})


def book(request):
    obj = Book.objects.all()
    if request.method == 'POST' and 'add' in request.POST:
        return redirect('bookform')
    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        ob = Book.objects.get(id=idd)
        ob.delete()
    return render(request, 'book.html', {'key': obj})


def Studentadmin(request):
    return render(request, 'studentadmin.html', {})


def addfee(request):
    fine = 0
    ob = ''
    obj1 = models.Student.objects.all()
    obj2 = models.Course.objects.all()
    obj3 = models.Batch.objects.all()
    obj4 = models.Category.objects.all()
    obj5 = models.Subcategory.objects.all()
    balance = None

    if request.method == "POST":
        admissionnumber = request.POST.get("admissionnumber")
        coursename = request.POST.get("course")
        batchname = request.POST.get("batch")
        feecategory = request.POST.get("category")
        subcategory = request.POST.get("subcategory")
        date = request.POST.get("date")
        duedate = request.POST.get("duedate")
        amt = request.POST.get("paid")
        paid = request.POST.get("paid")
        print(feecategory)
        # cat=models.Category.objects.get(category=feecategory)

        try:
            ob2 = models.Fee.objects.filter(admissionnumber=admissionnumber).last()
            balance = ob2.balance
        except:
            balance = 0

        obj = models.Fee()
        obj.admissionnumber = models.Student.objects.get(id=admissionnumber)
        obj.coursename = models.Course.objects.get(id=coursename)
        obj.batchname = models.Batch.objects.get(id=batchname)
        obj.feecategory = feecategory
        obj.subcategory = subcategory
        obj.amt = amt
        obj.paid = paid
        a = models.Category.objects.get(category=feecategory)

        if balance == 0:
            obj.balance = int(a.amount) - int(paid)
        if balance != 0:
            obj.balance = balance - int(paid)
            obj.save()

        obj.duedate = datetime.now() + timedelta(days=15)
        obj.save()
        delay = obj.duedate.day - obj.date.day
        if delay > 15:
            fine = fine + 10
        else:
            fine = 0
        obj.fine = fine
        obj.save()
        ob = models.Fee.objects.filter(admissionnumber=admissionnumber)

    return render(request, 'addfee.html',
                  {'key1': obj1, 'key2': obj2, 'key3': obj3, 'key4': obj4, 'key5': ob, 'key6': obj5})


def category(request):
    obj1 = models.Academicyear.objects.all()
    obj2 = models.Course.objects.all()
    obj3 = models.Category.objects.all()
    if request.method == "POST":
        academicyear = request.POST.get("academicyearname")
        course = request.POST.get("coursename")
        category = request.POST.get("category")
        subcategory = request.POST.get("subcategory")
        amount = request.POST.get("amount")
        date = request.POST.get("date")

        obj = Category()
        obj.academicyear = models.Academicyear.objects.get(id=academicyear)
        obj.course = models.Course.objects.get(id=course)
        obj.category = category
        obj.amount = amount
        obj.date = date
        obj.save()

    return render(request, 'category.html', {'key1': obj1, 'key2': obj2, 'key3': obj3})


def subcategory(request):
    obj1 = models.Course.objects.all()
    obj2 = models.Subcategory.objects.all()
    if request.method == "POST":
        course = request.POST.get("coursename")
        subcategory = request.POST.get("subcategory")

        obj = models.Subcategory()
        obj.course = models.Course.objects.get(id=course)
        obj.subcategory = subcategory
        obj.save()

    return render(request, 'subcategory.html', {'key1': obj1, 'key2': obj2})


def report(request):
    obj1 = models.Transport.objects.all()
    obj2 = models.Batch.objects.all()

    if request.method == "POST":
        course = request.POST.get("coursename")
        batch = request.POST.get("batchname")

        obj = category()
        obj.course = models.Course.objects.all()
        obj.batch = models.Batch.objects.all()
        obj.save()

    return render(request, 'report.html', {'key1': obj1, 'key2': obj2})


def addtransport(request):
    obj1 = models.Transport.objects.all()
    print(obj1)
    if request.method == 'POST':
        name = request.POST.get("routename")
        price = request.POST.get("transportprice")
        print(name, price)
        obj = Transport()
        obj.routename = name
        obj.transportprice = price
        obj.save()
        return redirect('transport')

    return render(request, 'addtransport.html', {'key1': obj1})


def edittransport(request, id):
    obj = Transport.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get("routename")
        price = request.POST.get("transportprice")

        obj.routename = name
        obj.transportprice = price
        obj.save()

        return redirect('transport')

    return render(request, 'edittransport.html', {'key': obj})


def transport(request):
    msg=''
    obj7= ''
    obj1 = models.Student.objects.all()
    obj2 = models.Course.objects.all()
    obj3 = models.Batch.objects.all()
    obj4 = models.Busroute.objects.all()
    obj5 = models.Transport.objects.all()
    obj6 = models.Assign.objects.all()
    if request.method == "POST":
        admissionnumber = request.POST.get("admissionnumber")
        course = request.POST.get("coursename")
        batch = request.POST.get("batchname")
        route = request.POST.get("routename")
        print(route,'pppppp')
        amount = request.POST.get("amount")
        obj7=models.Transport.objects.filter(admissionnumber=admissionnumber)
        if not obj7:
            print('+++++++dddddd')
            obj = Transport()
            obj.admissionnumber = models.Student.objects.get(id=admissionnumber)
            obj.coursename = models.Course.objects.get(id=course)
            obj.batchname = models.Batch.objects.get(id=batch)
            obj.route = models.Assign.objects.get(id=route)
            print(obj.route)
            obj.save()
        else:
            msg='yes'

    return render(request, 'transport.html',
                  {'key1': obj1, 'key2': obj2, 'key3': obj3, 'key4': obj4, 'key5': obj7, 'key6': obj6,'msg':msg})


def busdetails(request):
    obj1 = models.Busdetails.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Busdetails.objects.get(id=idd)
        obj.delete()
    return render(request, 'busdetails.html', {'key1': obj1})

def busadd(request):
    obj1=Busdetails.objects.all()
    if request.method=='POST':


            busnumber = request.POST.get("busnumber")
            buscapacity = request.POST.get("buscapacity")
            driver = request.POST.get("driver")

            obj = Busdetails()
            obj.busnumber = busnumber
            obj.buscapacity = buscapacity
            obj.driver = driver
            obj.save()
            return redirect('busdetails')
    return render(request, 'busadd.html', {'key1': obj1})

def busedit(request,id):
    ob=Busdetails.objects.get(id=id)
    ob1=Busdetails.objects.all()
    if request.method=='POST':
            busnumber = request.POST.get("busnumber")
            buscapacity = request.POST.get("buscapacity")
            driver = request.POST.get("driver")


            ob.busnumber = busnumber
            ob.buscapacity = buscapacity
            ob.driver = driver
            ob.save()
            return redirect('busdetails')
    return render(request, 'busedit.html', {'key1': ob})

def busstop(request):
    obj1 = models.Busdetails.objects.all()
    obj2 = models.Busstop.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Busstop.objects.get(id=idd)
        obj.delete()

    return render(request, 'busstop.html', {'key1': obj1, 'key2': obj2})



def stopadd(request):
    obj1 = models.Busdetails.objects.all()
    obj2 = models.Busstop.objects.all()
    if request.method == 'POST':
        busstop = request.POST.get("busstop")
        busroute = request.POST.get("busroute")
        description = request.POST.get("description")
        bno = request.POST.get("busnumber")

        obj = Busstop()
        obj.busstop = busstop
        obj.busroute = busroute
        obj.bno = models.Busdetails.objects.get(id=bno)
        obj.description = description
        obj.save()
        return redirect('busstop')
    return render(request, 'stopadd.html', {'key1': obj1, 'key2': obj2})

def stopedit(request,id):
    ob= models.Busstop.objects.get(id=id)
    obj1 = models.Busdetails.objects.all()
    obj2= models.Busstop.objects.all()
    if request.method == 'POST':
        busstop = request.POST.get("busstop")
        busroute = request.POST.get("busroute")
        description = request.POST.get("description")
        bno = request.POST.get("busnumber")

        ob.busstop = busstop
        ob.busroute = busroute
        ob.bno = models.Busdetails.objects.get(id=bno)
        ob.description = description
        ob.save()
        return redirect('busstop')
    return render(request, 'stopedit.html', {'key1': obj1, 'key2': obj2,'key3':ob})

def assign(request):
    obj1 = models.Busstop.objects.all()
    obj2 = models.Busroute.objects.all()
    obj3 = models.Assign.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Assign.objects.get(id=idd)
        obj.delete()
    return render(request, 'assign.html', {"key1": obj1, 'key2': obj2, 'key3': obj3})

def assignadd(request):
    obj1 = models.Busstop.objects.all()
    obj2 = models.Busroute.objects.all()
    obj3 = models.Assign.objects.all()

    if request.method == "POST":
        busstop = request.POST.get("busstop")
        busroute = request.POST.get("busroute")
        drop = request.POST.get("droptime")
        pick = request.POST.get("picktime")
        amount = request.POST.get("transportprice")

        obj = models.Assign()
        obj.busstop = models.Busstop.objects.get(id=busstop)
        obj.route = models.Busroute.objects.get(id=busroute)
        obj.Drop = drop
        obj.pick = pick
        obj.transportprice = amount
        obj.save()
        return redirect('assign')

    return render(request, 'assignadd.html', {"key1": obj1, 'key2': obj2, 'key3': obj3})


def assignedit(request,id):
    obj=models.Assign.objects.get(id=id)
    obj1 = models.Busstop.objects.all()
    obj2 = models.Busroute.objects.all()
    obj3 = models.Assign.objects.all()

    if request.method == "POST":
        busstop = request.POST.get("busstop")
        busroute = request.POST.get("busroute")
        drop = request.POST.get("droptime")
        pick = request.POST.get("picktime")
        amount = request.POST.get("transportprice")

        obj = models.Assign()
        obj.busstop = models.Busstop.objects.get(id=busstop)
        obj.route = models.Busroute.objects.get(id=busroute)
        obj.Drop = drop
        obj.pick = pick
        obj.transportprice = amount
        obj.save()
        return redirect('assign')
    return render(request, 'assignedit.html', {"key1": obj1, 'key2': obj2, 'key3': obj3,'key4':obj})


def busroute(request):
    obj1 = models.Busroute.objects.all()
    obj2 = models.Busdetails.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Busroute.objects.get(id=idd)
        obj.delete()

    return render(request, 'busroute.html', {'key1':obj1, 'key2':obj2})

def routeadd(request):

    obj1 = models.Busroute.objects.all()
    obj2 = models.Busdetails.objects.all()
    if request.method == 'POST':
        route = request.POST.get("busroute")
        busno = request.POST.get("busnumber")
        description = request.POST.get("description")

        obj = models.Busroute()
        obj.busno = models.Busdetails.objects.get(id=busno)
        obj.routename = route
        obj.desscription = description
        obj.save()
        return redirect('busroute')
    return render(request, 'routeadd.html', {'key1': obj1, 'key2': obj2})
def routeedit(request,id):
    ob  = models.Busroute.objects.get(id=id)
    obj1 = models.Busroute.objects.all()
    obj2 = models.Busdetails.objects.all()
    if request.method == 'POST':
        route = request.POST.get("busroute")
        busno = request.POST.get("busnumber")
        description = request.POST.get("description")

        ob.busno = models.Busdetails.objects.get(id=busno)
        ob.routename = route
        ob.desscription = description
        ob.save()
        return redirect('busroute')
    return render(request, 'routeedit.html', {'key1': obj1, 'key2': obj2,'key3':ob})

def fcategory(request):
    ob = Feecategory.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Feecategory.objects.get(id=idd)
        obj.delete()

    return render(request, 'fcategory.html', {'key1': ob})


def feeadd(request):
    if request.method == "POST":
        name = request.POST.get("fcategory")
        ob = models.Feecategory()
        ob.category = name
        ob.save()
        return redirect('fcategory')
    return render(request, 'feeadd.html', {})


def feeedit(request, id):
    ob = Feecategory.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("fcategory")
        ob.category = name
        ob.save()
        return redirect('fcategory')
    return render(request, 'feeedit.html', {'key': ob})


def feetype(request):
    fee = models.Feetype.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = Feecategory.objects.get(id=idd)
        obj.delete()

    return render(request, 'feetype.html', {"key1": fee})


def typeadd(request):
    if request.method == "POST":
        type = request.POST.get("feetype")
        ob = models.Feetype()
        ob.feetype = type
        ob.save()
        return redirect('feetype')

    return render(request, 'typeadd.html', {})


def typeedit(request, id):
    ob = models.Feetype.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("fcategory")
        ob.feetype = name
        ob.save()
        return redirect('feetype')
    return render(request, 'typeedit.html', {'key': ob})


def fsubcategory(request):
    obj1 = models.Feesubcategory.objects.all()

    if request.method == 'POST' and 'delete' in request.POST:
        idd = request.POST.get('delete')
        obj = models.Feesubcategory.objects.get(id=idd)
        obj.delete()

    return render(request, 'fsubcategory.html', {'key1': obj1})


def subadd(request):
    obj1 = models.Feecategory.objects.all()
    obj2 = models.Feetype.objects.all()

    if request.method == "POST":
        name = request.POST.get("feecategory")
        type = request.POST.get("feetype")
        amount = request.POST.get('amount')
        date = request.POST.get('fromdate')
        due = request.POST.get('duedate')

        obj = models.Feesubcategory()
        obj.category = models.Feecategory.objects.get(id=name)
        obj.feetype = models.Feetype.objects.get(id=type)
        obj.fromdate = date
        obj.Duedate = due
        obj.amount = amount
        obj.save()

        return redirect('fsubcategory')

    return render(request, 'subadd.html', {'key1': obj1, 'key2': obj2})


def subedit(request, id):
    ob = models.Feesubcategory.objects.get(id=id)
    obj1 = models.Feesubcategory.objects.all()
    if request.method == "POST":
        name = request.POST.get("category")
        type = request.POST.get("feetype")
        date = request.POST.get("fromdate")
        due = request.POST.get("duedate")
        amount = request.POST.get("amount")

        obj = models.Feesubcategory()
        obj.category = models.Feecategory.objects.get(category=name)
        obj.feetype = models.Feetype.objects.get(feetype=type)
        obj.fromdate = date
        obj.Duedate = due
        obj.amount = amount
        obj.save()
        return redirect('fsubcategory')
    return render(request, 'subedit.html', {'key': ob, 'key1': obj1})


def feeallocation(request):
    obj1 = models.Feeallocation.objects.all()

    if request.method == "POST" and 'delete' in request.POST:
        idd = request.POST.get("delete")
        obj = models.Feeallocation.objects.get(id=idd)
        obj.delete()

    return render(request, 'feeallocation.html', {'key1': obj1})

def alloedit(request,id):
    obj =models.Feeallocation.objects.get(id=id)
    obj1 = models.Feecategory.objects.all()
    obj2 = models.Feetype.objects.all()
    obj3 = models.Course.objects.all()
    if request.method == "POST":
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        name = request.POST.get("feecategory")
        type = request.POST.get("feetype")
        course = request.POST.get("coursename")
        amount = request.POST.get("amount")

        obj.category = models.Feecategory.objects.get(id=name)
        obj.type = models.Feetype.objects.get(id=type)
        obj.course = models.Course.objects.get(id=course)
        obj.amount = amount
        obj.Duedate = datetime.now() + timedelta(days=15)
        obj.save()

        return redirect('feeallocation')
    return render(request, 'alloedit.html', {'key1': obj1, 'key2': obj2, 'key3': obj3,'key4':obj})


def alloadd(request):
    obj1 = models.Feecategory.objects.all()
    obj2 = models.Feetype.objects.all()
    obj3 = models.Course.objects.all()
    if request.method == "POST":
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        name = request.POST.get("feecategory")
        type = request.POST.get("feetype")
        course = request.POST.get("coursename")
        amount = request.POST.get("amount")

        obj = models.Feeallocation()
        obj.category = models.Feecategory.objects.get(id=name)
        obj.type = models.Feetype.objects.get(id=type)
        obj.course = models.Course.objects.get(id=course)
        obj.amount = amount
        obj.Duedate = datetime.now() + timedelta(days=15)
        obj.save()

        return redirect('feeallocation')
    return render(request, 'alloadd.html', {'key1': obj1, 'key2': obj2, 'key3': obj3})


def feecollection(request, course=None, admno=None):
    obj1 = models.Course.objects.all().values()
    obj2 = models.Student.objects.all().values()
    obj3 = ''
    ob2 = ''
    ob1 = ''
    obj=''
    ob7=''
    msg=''
    balance = None
    if course and admno:
        ob = models.Student.objects.filter(AdmissionNumber=admno)
        obj3 = models.Feeallocation.objects.filter(course=course).values()

        for i in obj3:
            print(i)
            ob = models.Feecollection.objects.filter(fee__category_id=i['category_id'], admission_id=admno).last()
            if ob!=None:
                print('bbbbbbbbbbbbb')


                feecategory = models.Feecategory.objects.get(id=i['category_id'])
                feetype = models.Feetype.objects.get(id=i['type_id'])
                # amount = models.Feeallocation.get(id=i['amount_id'])

                i['category_name'] = feecategory.category
                i['feetype_name'] = feetype.feetype
                # i['amount_name'] = feeallocation.amount
                # print('aaaaaaaaa',i['categ_name'])
            else:
                feecategory = models.Feecategory.objects.get(id=i['category_id'])
                feetype = models.Feetype.objects.get(id=i['type_id'])
                # amount = models.Feeallocation.objects.get(id=i['amount_id'])

                i['category_name'] = feecategory.category
                i['feetype_name'] = feetype.feetype
                i['balance'] = i['amount']
                print('fffffffff')
    if request.method == 'POST' and 'submit' in request.POST:

        course = request.POST.get("coursename")
        admno = request.POST.get("admissionnumber")


        return redirect('/school/feecollection/' + str(course) + '/' + str(admno) + '/')
        # ob7 = models.Student.objects.filter(AdmissionNumber=admno)
    ob2 = models.Student.objects.filter(AdmissionNumber=admno)

    if request.method == 'POST' and 'save' in request.POST:
        paid = request.POST.get("paid")
        category = request.POST.get('category')
        # admno = request.POST.get('admissionnumber')
        amount = request.POST.get("amount")
        ob7 = models.Feecollection.objects.filter(fee__category_id = category,admission_id=admno)
        print('hhhhhhhhhhhh',ob7,category,admno)
        if not ob7:
            print('-------reshma---------')
            obj = models.Feecollection()
            obj.course = models.Course.objects.get(id=course)
            # obj.fee = models.Feeallocation.objects.get(category_id=category,course_id=course)
            obj.paid = paid

            if balance == None:
                obj.balance = int(amount) - int(paid)
            if balance != None:
                obj.balance = balance - int(paid)
            if obj.balance==0:
                obj.status='Paid'
            elif obj.balance<int(amount):
                obj.status='Partially Paid'
            else:
                obj.status='Unpaid'
            obj.save()
        else:
            last_fee = models.Feecollection.objects.filter(fee__category_id=category, admission=admno).last()
            last_fee.balance


    return render(request, 'feecollection.html',
                  {'key1':obj1,'key2':obj2,'key3':obj3,'key4':ob2,'key5':ob1,'key7':obj,'msg':msg,'key6':ob7})

