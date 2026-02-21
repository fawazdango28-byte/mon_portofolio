from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView
from .models import Profile, Skill, Project, Experience, Education, Contact
from .forms import ContactForm

def home(request):
    """Vue pour la page d'accueil"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_projects = Project.objects.all()[:6]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
    }
    return render(request, 'index.html', context)

def about(request):
    """Vue pour la page à propos"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'about.html', context)

def skills(request):
    """Vue pour la page des compétences"""
    programming_languages = Skill.objects.filter(skill_type='language')
    frameworks = Skill.objects.filter(skill_type='framework')
    databases = Skill.objects.filter(skill_type='database')
    tools = Skill.objects.filter(skill_type='tool')
    others = Skill.objects.filter(skill_type='other')
    
    context = {
        'programming_languages': programming_languages,
        'frameworks': frameworks,
        'databases': databases,
        'tools': tools,
        'others': others,
    }
    return render(request, 'skills.html', context)

def projects(request):
    """Vue pour la page des projets"""
    all_projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    
    # Filtrage par statut si spécifié
    status = request.GET.get('status')
    if status:
        all_projects = all_projects.filter(status=status)
    
    context = {
        'projects': all_projects,
        'featured_projects': featured_projects,
        'current_status': status,
    }
    return render(request, 'projects.html', context)

class ProjectDetailView(DetailView):
    """Vue détaillée d'un projet"""
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.exclude(
            pk=self.object.pk
        ).filter(
            technologies__in=self.object.technologies.all()
        ).distinct()[:3]
        return context

def contact(request):
    """Vue pour la page de contact"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder le message
            contact_message = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            
            # Envoyer un email (optionnel)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                    message=f"""
                    Nouveau message de contact depuis le portfolio:
                    
                    Nom: {form.cleaned_data['name']}
                    Email: {form.cleaned_data['email']}
                    Sujet: {form.cleaned_data['subject']}
                    
                    Message:
                    {form.cleaned_data['message']}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Erreur envoi email: {e}")
            
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = ContactForm()
    
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'contact.html', context)

def download_cv(request):
    """Vue pour télécharger le CV"""
    try:
        profile = Profile.objects.first()
        if profile and profile.cv_file:
            response = redirect(profile.cv_file.url)
            return response
        else:
            messages.error(request, 'CV non disponible.')
            return redirect('home')
    except Exception as e:
        messages.error(request, 'Erreur lors du téléchargement du CV.')
        return redirect('home')

# API Views pour AJAX
def projects_api(request):
    """API pour récupérer les projets via AJAX"""
    projects = Project.objects.all().values(
        'id', 'title', 'short_description', 'image', 
        'github_url', 'live_url', 'status'
    )
    return JsonResponse(list(projects), safe=False)

def skills_api(request):
    """API pour récupérer les compétences via AJAX"""
    skills = Skill.objects.all().values(
        'name', 'skill_type', 'proficiency', 'icon'
    )
    return JsonResponse(list(skills), safe=False)