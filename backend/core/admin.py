from django.contrib import admin
from .models import AgencyClient, AgencyProject, AgencyCampaign

@admin.register(AgencyClient)
class AgencyClientAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "email", "phone", "industry", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "company", "email"]

@admin.register(AgencyProject)
class AgencyProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "client_name", "project_type", "budget", "status", "created_at"]
    list_filter = ["project_type", "status"]
    search_fields = ["name", "client_name"]

@admin.register(AgencyCampaign)
class AgencyCampaignAdmin(admin.ModelAdmin):
    list_display = ["name", "client_name", "platform", "budget", "spent", "created_at"]
    list_filter = ["platform", "status"]
    search_fields = ["name", "client_name"]
