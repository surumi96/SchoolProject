from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class User(AbstractUser):
#     studclass=models.IntegerField(null=True, blank=True)
#     fine=models.IntegerField(null=True, blank=True)
from django.db.models import CharField


class Academicyear(models.Model):
    academicyearname=models.CharField(max_length=255, null=True, blank=True)
    startson=models.DateField()
    endson=models.DateField
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)


class Course(models.Model):
    coursename=models.CharField(max_length=255)
    code=models.CharField(max_length=255, null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    isactive=models.BooleanField(default=True, null=True,blank=True)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    academicid=models.ForeignKey(Academicyear,on_delete=models.PROTECT)

    def __int__(self):
        return self.academicid

class Batch(models.Model):
    batchname=models.CharField(max_length=255)
    courseid=models.ForeignKey(Course, on_delete=models.PROTECT)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    academicid = models.ForeignKey(Academicyear,null=True, blank=True, on_delete=models.PROTECT)


class Student(models.Model):
    AdmissionNumber=models.IntegerField(blank=True,null=True)
    AdmissionYear=models.IntegerField()
    FirstName=models.CharField(max_length=255)
    LastName=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    DOB=models.DateField()
    BloodGroup=models.CharField(max_length=255, null=True, blank=True)
    PhoneNumber=models.CharField(max_length=255)
    ContactDetails=models.CharField(max_length=255)
    Gender=models.CharField(max_length=255)
    RollNo=models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    Batch=models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
    academicyear=models.ForeignKey(Academicyear,on_delete=models.CASCADE,null=True,blank=True)



class Book(models.Model):
    BookName=models.CharField(max_length=255)
    AuthorName=models.CharField(max_length=255)
    Number=models.IntegerField()
    def __str__(self):
        return self.BookName


class Teacher(models.Model):
    Name=models.CharField(max_length=255)
    Designation=models.CharField(max_length=255)
    Education=models.CharField(max_length=255)
    Experiance=models.IntegerField()
    Gender=models.CharField(max_length=255)
    Subject=models.CharField(max_length=255, null=True, blank=True)


class Order(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    BookName = models.ForeignKey(Book, on_delete=models.CASCADE)
    issuedate = models.DateField(null=True,blank=True,auto_now_add=True)
    returndate = models.DateField(null=True,blank=True)


class Bloodgroup(models.Model):
    group = models.CharField(max_length=255)
    studentid=models.ForeignKey(Student, on_delete=models.PROTECT)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)



class Timetable(models.Model):
    Day=models.CharField(null=True, blank=True, max_length=255)
    subject1=models.CharField(null=True, blank=True, max_length=255)
    subject2=models.CharField(null=True, blank=True, max_length=255)
    subject3=models.CharField(null=True, blank=True, max_length=255)
    subject4=models.CharField(null=True, blank=True, max_length=255)
    subject5=models.CharField(null=True, blank=True, max_length=255)
    subject6=models.CharField(null=True, blank=True, max_length=255)
    batchname=models.ForeignKey(Batch, null=True, blank=True, on_delete=models.PROTECT)

class Category(models.Model):
        category = models.CharField(null=True, blank=True, max_length=255)
        academicyear = models.ForeignKey(Academicyear, null=True, blank=True, on_delete=models.PROTECT)
        course = models.ForeignKey(Course, null=True, blank=True, max_length=255, on_delete=models.PROTECT)
        subcategory = models.CharField(null=True, blank=True, max_length=255)
        amount = models.IntegerField(null=True,blank=True)

class Fee(models.Model):
    coursename=models.ForeignKey(Course,null=True, blank=True, on_delete=models.PROTECT)
    batchname=models.ForeignKey(Batch, null=True, blank=True, on_delete=models.PROTECT)
    feecategory=models.CharField(null=True, blank=True, max_length=255)
    subcategory=models.CharField(null=True, blank=True, max_length=255)
    admissionnumber=models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    paid=models.IntegerField(null=True, blank=True)
    balance=models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    duedate = models.DateField(null=True,blank=True)
    amt=models.IntegerField( null=True, blank=True)
    fine=models.IntegerField(null=True, blank=True)


class Subcategory(models.Model):
    subcategory = models.CharField(null=True, blank=True, max_length=255)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.PROTECT)


class Busdetails(models.Model):
    busnumber=models.IntegerField(null=True,blank=True,)
    buscapacity=models.IntegerField(null=True,blank=True)
    driver=models.CharField(max_length=255, null=True,blank=True,)

class Busstop(models.Model):
    busstop=models.CharField(max_length=255, null=True,blank=True)
    busroute=models.CharField(max_length=255, null=True,blank=True)
    description=models.CharField(max_length=255, null=True,blank=True)
    bno=models.ForeignKey(Busdetails,null=True,blank=True,on_delete=models.PROTECT)


class Busroute(models.Model):
    routename= models.CharField(max_length=255,null=True,blank=True)
    desscription= models.CharField(max_length=255,null=True,blank=True)
    busno=models.ForeignKey(Busdetails,null=True,blank=True,on_delete=models.PROTECT)

class Assign(models.Model):
    busstop = models.ForeignKey(Busstop,null=True, blank=True, on_delete=models.PROTECT)
    transportprice = models.IntegerField(null=True, blank=True)
    route = models.ForeignKey(Busroute,max_length=255, null=True,blank=True,on_delete=models.PROTECT)
    pick = models.CharField(max_length=255, null=True,blank=True)
    Drop = models.CharField(max_length=255, null=True,blank=True)


class Transport(models.Model):
    admissionnumber=models.ForeignKey(Student,null=True, blank=True, on_delete=models.PROTECT)
    coursename=models.ForeignKey(Course,null=True,blank=True, on_delete=models.PROTECT)
    batchname=models.ForeignKey(Batch, null=True, blank=True, on_delete=models.PROTECT)
    route=models.ForeignKey(Assign, null=True, blank=True, on_delete=models.PROTECT)

class Feecategory(models.Model):
    category=models.CharField(max_length=255,null=True,blank=True)

class Feetype(models.Model):
    feetype=models.CharField(max_length=255,null=True,blank=True)


class Feeallocation(models.Model):
    category=models.ForeignKey(Feecategory,null=True,blank=True,on_delete=models.PROTECT)
    type=models.ForeignKey(Feetype,null=True,blank=True,on_delete=models.PROTECT)
    course=models.ForeignKey(Course,null=True,blank=True,on_delete=models.PROTECT)
    amount=models.IntegerField()
    fromdate = models.DateField(auto_now=True)
    Duedate = models.DateField(null=True, blank=True)


class Feecollection(models.Model):
    fee=models.ForeignKey(Feeallocation,null=True,blank=True,on_delete=models.PROTECT)
    admission=models.ForeignKey(Student,null=True,blank=True,on_delete=models.PROTECT)
    course=models.ForeignKey(Course,null=True,blank=True,on_delete=models.PROTECT)
    paid=models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    status=models.CharField(max_length=255)
