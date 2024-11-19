from django.urls import path
from .views import EligibilityView

urlpatterns = [
    path('eligibility/', EligibilityView.as_view(), name='eligibility'),
]
