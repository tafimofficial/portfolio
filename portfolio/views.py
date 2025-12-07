from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Skill, Experience, Education, SocialLink, Profile
from .forms import ProjectForm, SkillForm, ExperienceForm, EducationForm, SocialLinkForm, ProfileForm

def home(request):
    context = {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'featured_projects': Project.objects.filter(featured=True),
        'projects': Project.objects.all(),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'education': Education.objects.all().order_by('-start_date'),
        'social_links': SocialLink.objects.all(),
    }
    return render(request, 'portfolio/home.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def public_project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list_public.html', {'projects': projects})

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def dashboard(request):
    context = {
        'projects_count': Project.objects.count(),
        'skills_count': Skill.objects.count(),
        'experiences_count': Experience.objects.count(),
        'education_count': Education.objects.count(),
        'social_links_count': SocialLink.objects.count(),
    }
    return render(request, 'portfolio/admin/dashboard.html', context)

# Project CRUD
@login_required
@user_passes_test(is_superuser)
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/admin/project_list.html', {'projects': projects})

@login_required
@user_passes_test(is_superuser)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/admin/project_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/admin/project_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'portfolio/admin/project_confirm_delete.html', {'project': project})

# Skill CRUD
@login_required
@user_passes_test(is_superuser)
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/admin/skill_list.html', {'skills': skills})

@login_required
@user_passes_test(is_superuser)
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'portfolio/admin/skill_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portfolio/admin/skill_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'portfolio/admin/skill_confirm_delete.html', {'skill': skill})

# Experience CRUD
@login_required
@user_passes_test(is_superuser)
def experience_list(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/admin/experience_list.html', {'experiences': experiences})

@login_required
@user_passes_test(is_superuser)
def experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'portfolio/admin/experience_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def experience_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'portfolio/admin/experience_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        return redirect('experience_list')
    return render(request, 'portfolio/admin/experience_confirm_delete.html', {'experience': experience})

# Education CRUD
@login_required
@user_passes_test(is_superuser)
def education_list(request):
    education_list = Education.objects.all().order_by('-start_date')
    return render(request, 'portfolio/admin/education_list.html', {'education_list': education_list})

@login_required
@user_passes_test(is_superuser)
def education_create(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = EducationForm()
    return render(request, 'portfolio/admin/education_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def education_update(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'portfolio/admin/education_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def education_delete(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('education_list')
    return render(request, 'portfolio/admin/education_confirm_delete.html', {'education': education})

# SocialLink CRUD
@login_required
@user_passes_test(is_superuser)
def social_link_list(request):
    social_links = SocialLink.objects.all()
    return render(request, 'portfolio/admin/social_link_list.html', {'social_links': social_links})

@login_required
@user_passes_test(is_superuser)
def social_link_create(request):
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('social_link_list')
    else:
        form = SocialLinkForm()
    return render(request, 'portfolio/admin/social_link_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def social_link_update(request, pk):
    social_link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        form = SocialLinkForm(request.POST, instance=social_link)
        if form.is_valid():
            form.save()
            return redirect('social_link_list')
    else:
        form = SocialLinkForm(instance=social_link)
    return render(request, 'portfolio/admin/social_link_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def social_link_delete(request, pk):
    social_link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        social_link.delete()
        return redirect('social_link_list')
    return render(request, 'portfolio/admin/social_link_confirm_delete.html', {'object': social_link})

# Profile Update
@login_required
@user_passes_test(is_superuser)
def profile_update(request):
    profile = Profile.objects.first() or Profile.objects.create(name="Your Name", bio="Your Bio")
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'portfolio/admin/profile_form.html', {'form': form})
