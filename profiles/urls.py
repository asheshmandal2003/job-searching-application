from django.urls import path
from .views import StudentProfileCreateView, StudentProfileDetailView

urlpatterns = [
    path('students/', StudentProfileCreateView.as_view(), name='student-profile-create'),
    path('students/<int:id>/', StudentProfileDetailView.as_view(), name='student-detail'),
]
