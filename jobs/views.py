from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

class JobListCreateView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailView(APIView):
    def get_object(self, id):
        try:
            return Job.objects.get(id=id)
        except Job.DoesNotExist:
            return None

    def get(self, request, id):
        job = self.get_object(id)
        if not job:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        job = self.get_object(id)
        if not job:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        job = self.get_object(id)
        if not job:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        job.delete()
        return Response({"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
