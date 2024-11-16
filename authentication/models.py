from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .enums import UserRole

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices(),  
        default=UserRole.STUDENT.value,
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['role', 'password']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} {self.last_name}: ({self.get_role_display()})"

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    profile_summary = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='student_skills')
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    resume_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class TPOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tpo_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    college = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100)
    website_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

