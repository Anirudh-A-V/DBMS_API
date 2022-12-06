from django.contrib import admin
from .models import Patient, Appointment, Payment, Test, TestReport, Companion

# Register your models here.

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Test)
admin.site.register(TestReport)
admin.site.register(Companion)
