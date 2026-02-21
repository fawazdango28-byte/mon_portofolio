from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Profile(models.Model):
    """Modèle pour les informations personnelles du développeur"""
    name = models.CharField(max_length=100, default="DANGO NADEY Abdoul Fawaz")
    title = models.CharField(max_length=200, default="Développeur Full-Stack")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = RichTextField()
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # Liens sociaux
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    """Modèle pour les compétences techniques"""
    SKILL_TYPES = [
        ('language', 'Langage de programmation'),
        ('framework', 'Framework'),
        ('database', 'Base de données'),
        ('tool', 'Outil'),
        ('other', 'Autre'),
    ]
    
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    proficiency = models.IntegerField(default=50, help_text="Niveau de maîtrise (0-100)")
    icon = models.CharField(max_length=100, blank=True, help_text="Classe CSS pour l'icône")
    
    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['skill_type', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"

class Project(models.Model):
    """Modèle pour les projets"""
    STATUS_CHOICES = [
        ('completed', 'Terminé'),
        ('in_progress', 'En cours'),
        ('planned', 'Planifié'),
    ]
    
    title = models.CharField(max_length=200)
    description = RichTextField()
    short_description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='projects/')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    technologies = models.ManyToManyField(Skill, related_name='projects')
    featured = models.BooleanField(default=False)
    
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

class Experience(models.Model):
    """Modèle pour l'expérience professionnelle"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = RichTextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Laisser vide si en cours")
    current = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} chez {self.company}"

class Education(models.Model):
    """Modèle pour la formation"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Contact(models.Model):
    """Modèle pour les messages de contact"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message de {self.name} - {self.subject}"
    








    