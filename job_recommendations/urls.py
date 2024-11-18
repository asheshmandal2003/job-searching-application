from django.urls import path
from .views import JobRecommendationsView

urlpatterns = [
    path('recommendations/<int:id>/', JobRecommendationsView.as_view(), name='job_recommendations'),
]