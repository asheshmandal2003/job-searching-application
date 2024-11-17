from django.urls import path
from .views import StudentProfileCreateView, StudentProfileDetailView, TPOProfileCreateView, TPOProfileDetailView, CompanyProfileCreateView, CompanyProfileDetailView

urlpatterns = [
    path('students/', StudentProfileCreateView.as_view(), name='student-profile-create'),
    path('students/<int:id>/', StudentProfileDetailView.as_view(), name='student-detail'),
    path('tpos/', TPOProfileCreateView.as_view(), name='tpo-profile-create'),
    path('tpos/<int:id>/', TPOProfileDetailView.as_view(), name='tpo-detail'),
    path('companies/', CompanyProfileCreateView.as_view(), name='company-profile-create'),
    path('companies/<int:id>/', CompanyProfileDetailView.as_view(), name='company-detail'),
]
