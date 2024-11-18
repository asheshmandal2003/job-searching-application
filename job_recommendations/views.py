from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import recommend_jobs_knn
from profiles.models import StudentProfile
from jobs.serializers import JobSerializer

# Create your views here.
class JobRecommendationsView(APIView):
    def get_object(self, id):
        try:
            return StudentProfile.objects.get(id=id)
        except StudentProfile.DoesNotExist:
            return None
        
    def get(self, request, id):
        profile = self.get_object(id)
        if not profile:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        recommendations = recommend_jobs_knn(profile)
        return Response(
            [
                {
                    "job": JobSerializer(job).data,
                    "percent_matches": round((score/recommendations[0][1])*100, 2)
                } for job, score in recommendations],
            status=status.HTTP_200_OK
        )
        

