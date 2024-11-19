from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import filter_by_eligibility

# Create your views here.
class EligibilityView(APIView):
    def post(self, request):
        students = filter_by_eligibility(request)
        return Response(students, status=status.HTTP_200_OK)