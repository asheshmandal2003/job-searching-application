from django.contrib import admin
from .models import User, Skill, StudentProfile, TPOProfile, CompanyProfile, Admin

# Register your models here.

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(StudentProfile)
admin.site.register(TPOProfile)
admin.site.register(CompanyProfile)
admin.site.register(Admin)