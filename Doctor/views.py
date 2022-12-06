from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Doctor/index.html")

def doctor(request):
    return render(request, "Doctor/doctor.html")

def department(request):
    return render(request, "Doctor/department.html")

def dutytime(request):
    return render(request, "Doctor/dutytime.html")

def doctordepartment(request):
    return render(request, "Doctor/doctordepartment.html")

# Compare this snippet from Doctor\forms.py: