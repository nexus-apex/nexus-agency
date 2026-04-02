from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import AgencyClient, AgencyProject, AgencyCampaign
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusAgency with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusagency.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if AgencyClient.objects.count() == 0:
            for i in range(10):
                AgencyClient.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    company=["TechVision Pvt Ltd","Global Solutions","Pinnacle Systems","Nova Enterprises","CloudNine Solutions","MetaForge Inc","DataPulse Analytics","QuantumLeap Tech","SkyBridge Corp","Zenith Innovations"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    industry=f"Sample {i+1}",
                    contract_value=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["active", "prospect", "churned"]),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 AgencyClient records created'))

        if AgencyProject.objects.count() == 0:
            for i in range(10):
                AgencyProject.objects.create(
                    name=f"Sample AgencyProject {i+1}",
                    client_name=f"Sample AgencyProject {i+1}",
                    project_type=random.choice(["branding", "web_design", "seo", "social_media", "content"]),
                    budget=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["proposal", "active", "completed", "on_hold"]),
                    deadline=date.today() - timedelta(days=random.randint(0, 90)),
                    progress=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 AgencyProject records created'))

        if AgencyCampaign.objects.count() == 0:
            for i in range(10):
                AgencyCampaign.objects.create(
                    name=f"Sample AgencyCampaign {i+1}",
                    client_name=f"Sample AgencyCampaign {i+1}",
                    platform=random.choice(["google", "facebook", "instagram", "linkedin"]),
                    budget=round(random.uniform(1000, 50000), 2),
                    spent=round(random.uniform(1000, 50000), 2),
                    leads=random.randint(1, 100),
                    status=random.choice(["active", "paused", "completed"]),
                    roi=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 AgencyCampaign records created'))
