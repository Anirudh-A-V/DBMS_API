from django.contrib import admin
from .models import Doctor, DutyTime, Department, DoctorDepartment

# Register your models here.


admin.site.register(Doctor)
admin.site.register(DutyTime)
admin.site.register(Department)
admin.site.register(DoctorDepartment)
