from django.db.models import F
from profiles.models import StudentProfile
from rest_framework.response import Response
from rest_framework import status

def filter_by_eligibility(request):
    branches = request.data.get('branches', [])
    min_cgpa = request.data.get('min_cgpa', 0)
    
    if not isinstance(branches, list) or not branches:
        return Response({"error": "Invalid or missing 'branches' parameter."}, status=status.HTTP_400_BAD_REQUEST)

    if not isinstance(min_cgpa, (int, float)):
        return Response({"error": "Invalid 'min_cgpa' parameter."}, status=status.HTTP_400_BAD_REQUEST)
    
    students = StudentProfile.objects.filter(
    branch__in=branches, 
    cgpa__gte=min_cgpa                    
    ).values(
    first_name=F('user__first_name'),  
    last_name=F('user__last_name'),
    email=F('user__email'),
    student_cgpa=F('cgpa'),                    
    student_branch=F('branch'),
    student_resume_url=F('resume_url')
    )    
    return list(students);