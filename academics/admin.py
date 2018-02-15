from django.contrib import admin
from .models import Subject, Grade, RollCall, Semester


admin.site.register(Subject)

admin.site.register(RollCall)

admin.site.register(Semester)

admin.site.register(Grade)
