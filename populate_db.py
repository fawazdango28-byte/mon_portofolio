# populate_db.py - Script pour peupler la base de données avec des données initiales
# Exécuter avec: python manage.py shell < populate_db.py

from main.models import Profile, Skill, Project, Experience, Education
from django.utils import timezone
from datetime import date

# Créer le profil principal
profile, created = Profile.objects.get_or_create(
    name="DANGO NADEY Abdoul Fawaz",
    defaults={
        'title': "Développeur Full-Stack",
        'email': "abdoulfawaz.dango@example.com",
        'phone': "+228 XX XX XX XX",
        'location': "Lomé, Togo",
        'bio': """
        <p>Développeur full-stack passionné avec une expertise approfondie en Python, Django, Flutter et technologies web modernes. 
        Je crée des solutions numériques innovantes qui allient performance technique et expérience utilisateur exceptionnelle.</p>
        
        <p>Avec plus de 3 ans d'expérience dans le développement d'applications web et mobile, 
        je maîtrise l'ensemble de la chaîne de développement, de la conception à la mise en production.</p>
        
        <p>Mon approche combine créativité technique, rigueur professionnelle et veille technologique constante 
        pour livrer des projets qui dépassent les attentes.</p>
        """,
        'github_url': "https://github.com/dangonadey",
        'linkedin_url': "https://linkedin.com/in/dangonadey-abdoulfawaz",
        'twitter_url': "https://twitter.com/dangonadey",
    }
)

# Créer les compétences - Langages de programmation
languages = [
    ('Python', 95, 'fab fa-python'),
    ('Dart', 85, 'fas fa-mobile-alt'),
    ('JavaScript', 80, 'fab fa-js-square'),
    ('HTML', 95, 'fab fa-html5'),
    ('CSS', 90, 'fab fa-css3-alt'),
    ('SQL', 75, 'fas fa-database'),
]

for lang_name, proficiency, icon in languages:
    Skill.objects.get_or_create(
        name=lang_name,
        skill_type='language',
        defaults={
            'proficiency': proficiency,
            'icon': icon
        }
    )

# Frameworks
frameworks = [
    ('Django', 90, 'fas fa-server'),
    ('Flutter', 85, 'fas fa-mobile-alt'),
    ('Bootstrap', 80, 'fab fa-bootstrap'),
    ('Django REST Framework', 85, 'fas fa-api'),
]

for fw_name, proficiency, icon in frameworks:
    Skill.objects.get_or_create(
        name=fw_name,
        skill_type='framework',
        defaults={
            'proficiency': proficiency,
            'icon': icon
        }
    )

# Bases de données
databases = [
    ('MySQL', 80, 'fas fa-database'),
    ('SQLite', 85, 'fas fa-database'),
    ('Firebase', 75, 'fab fa-google'),
    ('Supabase', 70, 'fas fa-cloud'),
]

for db_name, proficiency, icon in databases:
    Skill.objects.get_or_create(
        name=db_name,
        skill_type='database',
        defaults={
            'proficiency': proficiency,
            'icon': icon
        }
    )

# Outils
tools = [
    ('VS Code', 95, 'fas fa-code'),
    ('Android Studio', 80, 'fab fa-android'),
    ('StarUML', 75, 'fas fa-project-diagram'),
    ('Canva', 70, 'fas fa-palette'),
    ('Git', 85, 'fab fa-git-alt'),
]

for tool_name, proficiency, icon in tools:
    Skill.objects.get_or_create(
        name=tool_name,
        skill_type='tool',
        defaults={
            'proficiency': proficiency,
            'icon': icon
        }
    )

# Expériences professionnelles
experiences_data = [
    {
        'company': 'FreeLance',
        'position': 'Développeur Full-Stack',
        'location': 'Lomé, Togo',
        'start_date': date(2022, 1, 1),
        'current': True,
        'description': """
        <ul>
        <li>Développement d'applications web avec Django et Python</li>
        <li>Création d'applications mobiles cross-platform avec Flutter</li>
        <li>Conception et développement d'APIs RESTful</li>
        <li>Gestion de bases de données MySQL et Firebase</li>
        <li>Déploiement et maintenance d'applications web</li>
        </ul>
        """
    },
    {
        'company': 'TechStart Togo',
        'position': 'Développeur Junior',
        'location': 'Lomé, Togo',
        'start_date': date(2021, 6, 1),
        'end_date': date(2021, 12, 31),
        'current': False,
        'description': """
        <ul>
        <li>Développement d'interfaces utilisateur responsives</li>
        <li>Collaboration avec l'équipe de design pour l'intégration</li>
        <li>Participation au développement d'applications web</li>
        <li>Tests et débogage d'applications</li>
        </ul>
        """
    }
]

for exp_data in experiences_data:
    Experience.objects.get_or_create(
        company=exp_data['company'],
        position=exp_data['position'],
        defaults=exp_data
    )

# Formation
educations_data = [
    {
        'institution': 'Université de Lomé',
        'degree': 'Licence en Informatique',
        'field_of_study': 'Génie Logiciel',
        'start_date': date(2018, 10, 1),
        'end_date': date(2021, 7, 31),
        'grade': 'Mention Bien',
        'description': """
        <p>Formation approfondie en informatique avec spécialisation en génie logiciel. 
        Acquisition de solides bases en programmation, bases de données, et méthodologies de développement.</p>
        """
    },
    {
        'institution': 'Centre de Formation Technique',
        'degree': 'Certificat en Développement Web',
        'field_of_study': 'Technologies Web',
        'start_date': date(2020, 1, 1),
        'end_date': date(2020, 6, 30),
        'description': """
        <p>Formation pratique intensive sur les technologies web modernes incluant HTML5, CSS3, 
        JavaScript, et frameworks populaires.</p>
        """
    }
]

for edu_data in educations_data:
    Education.objects.get_or_create(
        institution=edu_data['institution'],
        degree=edu_data['degree'],
        defaults=edu_data
    )

# Projets exemple
projects_data = [
    {
        'title': 'E-Commerce Platform',
        'short_description': 'Plateforme e-commerce complète avec Django et système de paiement intégré.',
        'description': """
        <p>Développement d'une plateforme e-commerce complète utilisant Django pour le backend et Bootstrap pour le frontend.</p>
        <h4>Fonctionnalités principales :</h4>
        <ul>
        <li>Système d'authentification et gestion des utilisateurs</li>
        <li>Catalogue de produits avec recherche et filtrage</li>
        <li>Panier d'achat et système de commandes</li>
        <li>Interface d'administration pour la gestion des produits</li>
        <li>Système de paiement sécurisé</li>
        </ul>
        """,
        'status': 'completed',
        'featured': True,
        'start_date': date(2023, 3, 1),
        'end_date': date(2023, 6, 30),
        'github_url': 'https://github.com/dangonadey/ecommerce-platform',
        'live_url': 'https://ecommerce-demo.example.com',
    },
    {
        'title': 'Task Manager Mobile App',
        'short_description': 'Application mobile de gestion de tâches développée avec Flutter.',
        'description': """
        <p>Application mobile cross-platform pour la gestion des tâches quotidiennes, développée avec Flutter et Dart.</p>
        <h4>Fonctionnalités :</h4>
        <ul>
        <li>Création et organisation des tâches par catégories</li>
        <li>Système de notifications et rappels</li>
        <li>Synchronisation cloud avec Firebase</li>
        <li>Interface utilisateur intuitive et moderne</li>
        <li>Mode hors-ligne avec synchronisation automatique</li>
        </ul>
        """,
        'status': 'completed',
        'featured': True,
        'start_date': date(2023, 7, 1),
        'end_date': date(2023, 9, 15),
        'github_url': 'https://github.com/dangonadey/task-manager-flutter',
    },
    {
        'title': 'Portfolio Website',
        'short_description': 'Site web portfolio personnel développé avec Django.',
        'description': """
        <p>Développement de ce site portfolio utilisant Django, Bootstrap et JavaScript moderne.</p>
        <h4>Caractéristiques techniques :</h4>
        <ul>
        <li>Interface responsive et moderne</li>
        <li>Système de gestion de contenu intégré</li>
        <li>Optimisation SEO</li>
        <li>Animations et interactions fluides</li>
        <li>Formulaire de contact fonctionnel</li>
        </ul>
        """,
        'status': 'completed',
        'featured': True,
        'start_date': date(2023, 10, 1),
        'end_date': date(2023, 11, 15),
        'github_url': 'https://github.com/dangonadey/portfolio-django',
    },
    {
        'title': 'API REST pour Blog',
        'short_description': 'API RESTful complète pour application de blog avec Django REST Framework.',
        'description': """
        <p>Développement d'une API REST complète pour une application de blog utilisant Django REST Framework.</p>
        <h4>Fonctionnalités de l'API :</h4>
        <ul>
        <li>CRUD complet pour les articles de blog</li>
        <li>Système d'authentification JWT</li>
        <li>Gestion des commentaires et likes</li>
        <li>Pagination et filtrage avancé</li>
        <li>Documentation automatique avec Swagger</li>
        </ul>
        """,
        'status': 'completed',
        'featured': False,
        'start_date': date(2023, 1, 1),
        'end_date': date(2023, 2, 28),
        'github_url': 'https://github.com/dangonadey/blog-api-django',
    },
    {
        'title': 'Weather App Flutter',
        'short_description': 'Application météo avec géolocalisation développée en Flutter.',
        'description': """
        <p>Application mobile météo avec géolocalisation automatique et prévisions détaillées.</p>
        <h4>Fonctionnalités :</h4>
        <ul>
        <li>Géolocalisation automatique</li>
        <li>Prévisions météo sur 7 jours</li>
        <li>Interface utilisateur élégante</li>
        <li>Notifications météo personnalisées</li>
        <li>Mode sombre/clair</li>
        </ul>
        """,
        'status': 'in_progress',
        'featured': False,
        'start_date': date(2023, 11, 1),
        'github_url': 'https://github.com/dangonadey/weather-flutter',
    }
]

# Créer les projets et associer les technologies
for proj_data in projects_data:
    project, created = Project.objects.get_or_create(
        title=proj_data['title'],
        defaults=proj_data
    )
    
    # Associer les technologies selon le type de projet
    if 'Django' in proj_data['title'] or 'E-Commerce' in proj_data['title'] or 'API' in proj_data['title'] or 'Portfolio' in proj_data['title']:
        django_skill = Skill.objects.get(name='Django')
        python_skill = Skill.objects.get(name='Python')
        html_skill = Skill.objects.get(name='HTML')
        css_skill = Skill.objects.get(name='CSS')
        js_skill = Skill.objects.get(name='JavaScript')
        project.technologies.add(django_skill, python_skill, html_skill, css_skill, js_skill)
    
    if 'Flutter' in proj_data['title'] or 'Mobile' in proj_data['title'] or 'Weather' in proj_data['title']:
        flutter_skill = Skill.objects.get(name='Flutter')
        dart_skill = Skill.objects.get(name='Dart')
        firebase_skill = Skill.objects.get(name='Firebase')
        project.technologies.add(flutter_skill, dart_skill, firebase_skill)

print("✅ Base de données peuplée avec succès!")
print("Données créées:")
print(f"- 1 Profil: {profile.name}")
print(f"- {Skill.objects.count()} Compétences")
print(f"- {Experience.objects.count()} Expériences")
print(f"- {Education.objects.count()} Formations")
print(f"- {Project.objects.count()} Projets")
print("\n🚀 Vous pouvez maintenant lancer le serveur avec: python manage.py runserver")
print("📱 Interface admin accessible sur: http://127.0.0.1:8000/admin/")
print("🌐 Site accessible sur: http://127.0.0.1:8000/")