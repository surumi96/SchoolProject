from django.contrib import admin
from .models import Teacher, Student, Batch,Academicyear,Course


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Batch)
admin.site.register(Academicyear)
admin.site.register(Course)