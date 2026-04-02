from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('agencyclients/', views.agencyclient_list, name='agencyclient_list'),
    path('agencyclients/create/', views.agencyclient_create, name='agencyclient_create'),
    path('agencyclients/<int:pk>/edit/', views.agencyclient_edit, name='agencyclient_edit'),
    path('agencyclients/<int:pk>/delete/', views.agencyclient_delete, name='agencyclient_delete'),
    path('agencyprojects/', views.agencyproject_list, name='agencyproject_list'),
    path('agencyprojects/create/', views.agencyproject_create, name='agencyproject_create'),
    path('agencyprojects/<int:pk>/edit/', views.agencyproject_edit, name='agencyproject_edit'),
    path('agencyprojects/<int:pk>/delete/', views.agencyproject_delete, name='agencyproject_delete'),
    path('agencycampaigns/', views.agencycampaign_list, name='agencycampaign_list'),
    path('agencycampaigns/create/', views.agencycampaign_create, name='agencycampaign_create'),
    path('agencycampaigns/<int:pk>/edit/', views.agencycampaign_edit, name='agencycampaign_edit'),
    path('agencycampaigns/<int:pk>/delete/', views.agencycampaign_delete, name='agencycampaign_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
