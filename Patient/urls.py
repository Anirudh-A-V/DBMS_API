from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("patient/", views.patient, name="patient"),
    path("appointment/", views.appointment, name="appointment"),
    path("payment/", views.payment, name="payment"),
    path("test/", views.test, name="test"),
    path("testreport/", views.testreport, name="testreport"),
    path("companion/", views.companion, name="companion"),
]
