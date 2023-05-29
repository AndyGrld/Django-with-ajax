from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Student)


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass
