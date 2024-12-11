from django.urls import path
from .views import EligibilityView, EligibilityEmailsView, SendEmailsView

urlpatterns = [
    path('eligibility/', EligibilityView.as_view(), name='eligibility'),
    path('eligibility/emails/', EligibilityEmailsView.as_view(), name='eligibility-emails'),
    path('eligibility/send_emails/', SendEmailsView.as_view(), name='send-emails'),
]
