from django.contrib import admin
from .models import StudentProfile, TPOProfile, CompanyProfile, AdminProfile

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(TPOProfile)
admin.site.register(CompanyProfile)
admin.site.register(AdminProfile)
