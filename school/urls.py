"""ProjectSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Login_view, name='login'),
    path('form/', views.Form, name='form'),
    path('admin/', views.Admin_view, name='admin'),
    path('studentadmin/', views.Studentadmin, name='studentadmin'),
    path('studentlist/',views.Studentlist, name='studentlist'),
    path('editstudent/<int:id>/',views.Editstudent, name='editstudent'),
    path('order/', views.order, name='order'),
    path('history/', views.history, name='history'),
    path('admission/', views.Admission, name='admission'),

    path('book/',views.book, name="book"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('bookform/', views.bookform, name="bookform"),
    path('editbook/<int:id>/', views.editbook, name="editbook"),
    path('search/', views.search, name="search"),
    path('teacherdetails/', views.teacherdetails, name='teacherdetails'),
    path('timetable/', views.timetable, name='timetable'),
    path('teacherlist/', views.teacherlist, name='teacherlist'),
    path('course/', views.Course_view, name="course"),
    path('academicyear/',views.Academicyear, name="academicyear"),
    path('batch/',views.Batch, name="batch"),
    path('addfee/', views.addfee, name="addfee"),
    path('category/', views.category, name="category"),
    path('subcategory/',views.subcategory, name='subcategory'),
    path('report/', views.report, name='report'),
    path('transport/', views.transport, name='transport'),
    path('addtransport/', views.addtransport, name='addtransport'),
    path('edittransport/<int:id>/', views.edittransport, name="edittransport"),
    path('assign/', views.assign, name="assign"),
    path('busdetails/',views.busdetails, name='busdetails'),
    path('busstop/', views.busstop, name='busstop'),
    path('busroute/', views.busroute, name='busroute')
]