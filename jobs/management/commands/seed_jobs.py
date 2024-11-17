import random
from django.core.management.base import BaseCommand
from jobs.models import Job
from profiles.models import CompanyProfile
from skills.models import Skill

class Command(BaseCommand):
    help = "Seed the database with job data for testing"

    def handle(self, *args, **kwargs):
        Job.objects.all().delete()
        self.stdout.write(self.style.WARNING("Deleted all existing jobs."))
        
        companies = CompanyProfile.objects.all()
        skills = Skill.objects.all()
        
        if not companies.exists():
            self.stdout.write(self.style.ERROR("No companies found. Create some CompanyProfiles first."))
            return

        if not skills.exists():
            self.stdout.write(self.style.ERROR("No skills found. Create some Skills first."))
            return

        job_types = ['FULL_TIME', 'INTERNSHIP']
        locations = ['India', 'New York', 'San Francisco', 'Remote', 'Boston', 'London']

        for i in range(100): 
            company = random.choice(companies)
            required_skills = random.sample(list(skills), k=min(len(skills), random.randint(2, 5)))

            job = Job.objects.create(
                company=company,
                title=f"Job Title {i + 1}",
                description=f"This is a description for job {i + 1}.",
                location=random.choice(locations),
                salary=random.uniform(50000, 150000),
                job_type=random.choice(job_types),
            )
            job.required_skills.set(required_skills)
            job.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully created 100 job entries."))
