from django.db import models
from authentication.models import CompanyProfile, Skill
from .enums import JobType

# Create your models here.

class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    required_skills = models.ManyToManyField(Skill, related_name='jobs')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    job_type = models.CharField(
        max_length=20,
        choices= JobType.choices(),
        default=JobType.FULL_TIME.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
