import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import AgencyClient, AgencyProject, AgencyCampaign


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['agencyclient_count'] = AgencyClient.objects.count()
    ctx['agencyclient_active'] = AgencyClient.objects.filter(status='active').count()
    ctx['agencyclient_prospect'] = AgencyClient.objects.filter(status='prospect').count()
    ctx['agencyclient_churned'] = AgencyClient.objects.filter(status='churned').count()
    ctx['agencyclient_total_contract_value'] = AgencyClient.objects.aggregate(t=Sum('contract_value'))['t'] or 0
    ctx['agencyproject_count'] = AgencyProject.objects.count()
    ctx['agencyproject_branding'] = AgencyProject.objects.filter(project_type='branding').count()
    ctx['agencyproject_web_design'] = AgencyProject.objects.filter(project_type='web_design').count()
    ctx['agencyproject_seo'] = AgencyProject.objects.filter(project_type='seo').count()
    ctx['agencyproject_total_budget'] = AgencyProject.objects.aggregate(t=Sum('budget'))['t'] or 0
    ctx['agencycampaign_count'] = AgencyCampaign.objects.count()
    ctx['agencycampaign_google'] = AgencyCampaign.objects.filter(platform='google').count()
    ctx['agencycampaign_facebook'] = AgencyCampaign.objects.filter(platform='facebook').count()
    ctx['agencycampaign_instagram'] = AgencyCampaign.objects.filter(platform='instagram').count()
    ctx['agencycampaign_total_budget'] = AgencyCampaign.objects.aggregate(t=Sum('budget'))['t'] or 0
    ctx['recent'] = AgencyClient.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def agencyclient_list(request):
    qs = AgencyClient.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'agencyclient_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def agencyclient_create(request):
    if request.method == 'POST':
        obj = AgencyClient()
        obj.name = request.POST.get('name', '')
        obj.company = request.POST.get('company', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.industry = request.POST.get('industry', '')
        obj.contract_value = request.POST.get('contract_value') or 0
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/agencyclients/')
    return render(request, 'agencyclient_form.html', {'editing': False})


@login_required
def agencyclient_edit(request, pk):
    obj = get_object_or_404(AgencyClient, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.company = request.POST.get('company', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.industry = request.POST.get('industry', '')
        obj.contract_value = request.POST.get('contract_value') or 0
        obj.status = request.POST.get('status', '')
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/agencyclients/')
    return render(request, 'agencyclient_form.html', {'record': obj, 'editing': True})


@login_required
def agencyclient_delete(request, pk):
    obj = get_object_or_404(AgencyClient, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/agencyclients/')


@login_required
def agencyproject_list(request):
    qs = AgencyProject.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(project_type=status_filter)
    return render(request, 'agencyproject_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def agencyproject_create(request):
    if request.method == 'POST':
        obj = AgencyProject()
        obj.name = request.POST.get('name', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.project_type = request.POST.get('project_type', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.deadline = request.POST.get('deadline') or None
        obj.progress = request.POST.get('progress') or 0
        obj.save()
        return redirect('/agencyprojects/')
    return render(request, 'agencyproject_form.html', {'editing': False})


@login_required
def agencyproject_edit(request, pk):
    obj = get_object_or_404(AgencyProject, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.project_type = request.POST.get('project_type', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.deadline = request.POST.get('deadline') or None
        obj.progress = request.POST.get('progress') or 0
        obj.save()
        return redirect('/agencyprojects/')
    return render(request, 'agencyproject_form.html', {'record': obj, 'editing': True})


@login_required
def agencyproject_delete(request, pk):
    obj = get_object_or_404(AgencyProject, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/agencyprojects/')


@login_required
def agencycampaign_list(request):
    qs = AgencyCampaign.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(platform=status_filter)
    return render(request, 'agencycampaign_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def agencycampaign_create(request):
    if request.method == 'POST':
        obj = AgencyCampaign()
        obj.name = request.POST.get('name', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.platform = request.POST.get('platform', '')
        obj.budget = request.POST.get('budget') or 0
        obj.spent = request.POST.get('spent') or 0
        obj.leads = request.POST.get('leads') or 0
        obj.status = request.POST.get('status', '')
        obj.roi = request.POST.get('roi') or 0
        obj.save()
        return redirect('/agencycampaigns/')
    return render(request, 'agencycampaign_form.html', {'editing': False})


@login_required
def agencycampaign_edit(request, pk):
    obj = get_object_or_404(AgencyCampaign, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.platform = request.POST.get('platform', '')
        obj.budget = request.POST.get('budget') or 0
        obj.spent = request.POST.get('spent') or 0
        obj.leads = request.POST.get('leads') or 0
        obj.status = request.POST.get('status', '')
        obj.roi = request.POST.get('roi') or 0
        obj.save()
        return redirect('/agencycampaigns/')
    return render(request, 'agencycampaign_form.html', {'record': obj, 'editing': True})


@login_required
def agencycampaign_delete(request, pk):
    obj = get_object_or_404(AgencyCampaign, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/agencycampaigns/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['agencyclient_count'] = AgencyClient.objects.count()
    data['agencyproject_count'] = AgencyProject.objects.count()
    data['agencycampaign_count'] = AgencyCampaign.objects.count()
    return JsonResponse(data)
