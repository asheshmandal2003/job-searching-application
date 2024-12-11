from django.db.models import F
from profiles.models import StudentProfile
from rest_framework.response import Response
from rest_framework import status
from django.contrib.postgres.aggregates import ArrayAgg
from django.core.mail import send_mail

def check_fields(branches, min_cgpa, skills):
    if not isinstance(branches, list) or not branches:
        return Response({"error": "Invalid or missing 'branches' parameter."}, status=status.HTTP_400_BAD_REQUEST)

    if not isinstance(min_cgpa, (int, float)):
        return Response({"error": "Invalid 'min_cgpa' parameter."}, status=status.HTTP_400_BAD_REQUEST)
    
    if not isinstance(skills, list):
        return Response({"error": "Invalid 'skills' parameter."}, status=status.HTTP_400_BAD_REQUEST)
    return None

def filter_by_eligibility(request):
    branches = request.data.get('branches', [])
    min_cgpa = request.data.get('min_cgpa', 0)
    skills = request.data.get('skills', [])
    
    check_fields(branches, min_cgpa, skills)
    
    students = StudentProfile.objects.filter(
    branch__in=branches, 
    cgpa__gte=min_cgpa ,
    skills__name__in=skills                   
    ).values(
    student_first_name=F('first_name'),  
    student_last_name=F('last_name'),
    email=F('user__email'),
    student_profile_summary=F('profile_summary'),
    student_cgpa=F('cgpa'),                    
    student_branch=F('branch'),
    student_resume_url=F('resume_url'),
    student_skills=ArrayAgg('skills__name', distinct=True)  
    )    
    return list(students);

def get_eligible_students_emails(branch, min_cgpa, skills):
    students = StudentProfile.objects.filter(
    branch=branch, 
    cgpa__gte=min_cgpa ,
    skills__name__in=skills                   
    ).values_list('user__email', flat=True)
    return list(students);

def get_students_emails(request):
    branches = request.data.get('branches', [])
    min_cgpa = request.data.get('min_cgpa', 0)
    skills = request.data.get('skills', [])
    
    check_fields(branches, min_cgpa, skills)
    
    students = StudentProfile.objects.filter(
    branch__in=branches, 
    cgpa__gte=min_cgpa ,
    skills__name__in=skills                   
    ).values_list('user__email', flat=True)
    return list(students);


def send_email(request):
    subject = request.data.get('subject', 'New Job Opportunity')
    message = request.data.get('message', 'Description of the job opportunity.')
    from_email = request.data.get('from_email', '')
    recipient_list = request.data.get('recipient_list', [])
    
    send_mail(subject, message, from_email, recipient_list)
