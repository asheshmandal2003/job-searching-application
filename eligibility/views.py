from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import filter_by_eligibility, get_students_emails, send_email

# Create your views here.
class EligibilityView(APIView):
    def get(self, request):
        students = filter_by_eligibility(request)
        return Response(students, status=status.HTTP_200_OK)
    
class EligibilityEmailsView(APIView):
    def get(self, request):
        students = get_students_emails(request)
        return Response(students, status=status.HTTP_200_OK)
    
class SendEmailsView(APIView):
    def post(self, request):
        send_email(request)
        return Response({"message": "Emails sent successfully."}, status=status.HTTP_200_OK)