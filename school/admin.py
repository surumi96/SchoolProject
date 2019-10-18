from django.contrib import admin
from .models import Teacher, Student, Batch,Academicyear,Course,Fee,Category,Subcategory


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Batch)
admin.site.register(Academicyear)
admin.site.register(Course)
admin.site.register(Fee)
admin.site.register(Category)
admin.site.register(Subcategory)