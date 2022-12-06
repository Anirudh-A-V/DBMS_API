from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doctor/", views.doctor, name="doctor"),
    path("department/", views.department, name="department"),
    path("dutytime/", views.dutytime, name="dutytime"),
    path("doctordepartment/", views.doctordepartment, name="doctordepartment"),
]


