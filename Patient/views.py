from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Patient/index.html")

def patient(request):
    return render(request, "Patient/patient.html")

def appointment(request):
    return render(request, "Patient/appointment.html")

def payment(request):
    return render(request, "Patient/payment.html")

def test(request):
    return render(request, "Patient/test.html")

def testreport(request):
    return render(request, "Patient/testreport.html")

def companion(request):
    return render(request, "Patient/companion.html")