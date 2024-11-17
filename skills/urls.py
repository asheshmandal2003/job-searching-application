from django.urls import path
from .views import SkillsListCreateView, SkillDetailView

urlpatterns = [
    path('skills/', SkillsListCreateView.as_view(), name='skills-list-create'),
    path('skills/<int:id>/', SkillDetailView.as_view(), name='skill-detail'),
]
