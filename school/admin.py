from django.contrib import admin
from .models import Teacher, Student, Batch,Academicyear,Course,Fee,Category,Subcategory,Transport,Assign,Busdetails,Busstop
from.models import Busroute

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Batch)
admin.site.register(Academicyear)
admin.site.register(Course)
admin.site.register(Fee)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Transport)
admin.site.register(Assign)
admin.site.register(Busdetails)
admin.site.register(Busstop)
admin.site.register(Busroute)