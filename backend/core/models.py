from django.db import models

class AgencyClient(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    industry = models.CharField(max_length=255, blank=True, default="")
    contract_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("prospect", "Prospect"), ("churned", "Churned")], default="active")
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class AgencyProject(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, default="")
    project_type = models.CharField(max_length=50, choices=[("branding", "Branding"), ("web_design", "Web Design"), ("seo", "SEO"), ("social_media", "Social Media"), ("content", "Content")], default="branding")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("proposal", "Proposal"), ("active", "Active"), ("completed", "Completed"), ("on_hold", "On Hold")], default="proposal")
    deadline = models.DateField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class AgencyCampaign(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, default="")
    platform = models.CharField(max_length=50, choices=[("google", "Google"), ("facebook", "Facebook"), ("instagram", "Instagram"), ("linkedin", "LinkedIn")], default="google")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    leads = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("paused", "Paused"), ("completed", "Completed")], default="active")
    roi = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
