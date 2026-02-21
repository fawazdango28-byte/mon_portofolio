from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Experience, Education, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('name', 'title', 'email', 'phone', 'location', 'bio', 'profile_image', 'cv_file')
        }),
        ('Liens sociaux', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'portfolio_url')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # Empêcher la création de multiples profils
        if Profile.objects.exists():
            return False
        return True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_type', 'proficiency', 'proficiency_bar']
    list_filter = ['skill_type']
    search_fields = ['name']
    ordering = ['skill_type', 'name']
    
    def proficiency_bar(self, obj):
        width = obj.proficiency
        color = 'success' if width >= 80 else 'warning' if width >= 60 else 'danger'
        return format_html(
            '<div class="progress" style="width: 100px;"><div class="progress-bar bg-{}" role="progressbar" style="width: {}%"></div></div>',
            color, width
        )
    proficiency_bar.short_description = 'Niveau'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'start_date', 'project_image', 'created_at']
    list_filter = ['status', 'featured', 'start_date', 'technologies']
    search_fields = ['title', 'short_description']
    ordering = ['-created_at']
    filter_horizontal = ['technologies']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'short_description', 'description', 'image', 'status', 'featured')
        }),
        ('Liens', {
            'fields': ('github_url', 'live_url')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
    )
    
    def project_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Pas d'image"
    project_image.short_description = 'Image'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date', 'company']
    search_fields = ['position', 'company', 'location']
    ordering = ['-start_date']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('company', 'position', 'location', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'current')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'grade']
    list_filter = ['start_date', 'institution']
    search_fields = ['degree', 'institution', 'field_of_study']
    ordering = ['-start_date']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('institution', 'degree', 'field_of_study', 'description', 'grade')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Expéditeur', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'read')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Marquer comme lu"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)
    mark_as_unread.short_description = "Marquer comme non lu"
    
    actions = ['mark_as_read', 'mark_as_unread']

# Personnalisation de l'interface d'administration
admin.site.site_header = "Portfolio DANGO NADEY Abdoul Fawaz"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Administration du Portfolio"