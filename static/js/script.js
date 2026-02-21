// Script principal pour le portfolio Django
document.addEventListener('DOMContentLoaded', function() {
    // Initialisation d'AOS (Animate On Scroll)
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100
        });
    }

    // Gestion du bouton "Retour en haut"
    const backToTopButton = document.getElementById('backToTop');
    
    if (backToTopButton) {
        // Afficher/masquer le bouton selon le scroll
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('show');
            } else {
                backToTopButton.classList.remove('show');
            }
        });

        // Action du clic sur le bouton
        backToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Gestion de la navbar au scroll
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.style.background = 'rgba(33, 37, 41, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.style.background = '';
            navbar.style.backdropFilter = '';
        }
        
        lastScrollTop = scrollTop;
    });

    // Animation des barres de progression (compétences)
    const skillBars = document.querySelectorAll('.skill-progress-bar');
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };

    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const percentage = progressBar.dataset.percentage;
                progressBar.style.width = percentage + '%';
            }
        });
    }, observerOptions);

    skillBars.forEach(bar => {
        skillObserver.observe(bar);
    });

    // Gestion du formulaire de contact avec validation
    const contactForm = document.querySelector('form[action*="contact"]');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const nameField = contactForm.querySelector('input[name="name"]');
            const emailField = contactForm.querySelector('input[name="email"]');
            const messageField = contactForm.querySelector('textarea[name="message"]');
            
            let isValid = true;
            
            // Validation du nom
            if (!nameField.value.trim()) {
                showFieldError(nameField, 'Le nom est requis');
                isValid = false;
            } else {
                clearFieldError(nameField);
            }
            
            // Validation de l'email
            if (!emailField.value.trim()) {
                showFieldError(emailField, 'L\'email est requis');
                isValid = false;
            } else if (!isValidEmail(emailField.value)) {
                showFieldError(emailField, 'Veuillez entrer un email valide');
                isValid = false;
            } else {
                clearFieldError(emailField);
            }
            
            // Validation du message
            if (!messageField.value.trim()) {
                showFieldError(messageField, 'Le message est requis');
                isValid = false;
            } else if (messageField.value.trim().length < 10) {
                showFieldError(messageField, 'Le message doit contenir au moins 10 caractères');
                isValid = false;
            } else {
                clearFieldError(messageField);
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // Fonction pour afficher les erreurs de champ
    function showFieldError(field, message) {
        clearFieldError(field);
        field.classList.add('is-invalid');
        
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }

    // Fonction pour effacer les erreurs de champ
    function clearFieldError(field) {
        field.classList.remove('is-invalid');
        const errorDiv = field.parentNode.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.remove();
        }
    }

    // Fonction de validation d'email
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Animation des compteurs (statistiques)
    const counters = document.querySelectorAll('.stats-number');
    
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.dataset.count || counter.textContent);
                let current = 0;
                const increment = target / 50;
                
                const updateCounter = () => {
                    if (current < target) {
                        current += increment;
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                
                updateCounter();
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    // Filtrage des projets par statut (data-status sur .project-item)
    const filterButtons = document.querySelectorAll('.project-filter');
    const projectItems = document.querySelectorAll('.project-item');

    if (filterButtons.length > 0 && projectItems.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                // Retirer active de tous les boutons
                filterButtons.forEach(b => b.classList.remove('active'));
                this.classList.add('active');

                const filter = this.getAttribute('data-filter');

                projectItems.forEach(item => {
                    if (filter === 'all' || item.getAttribute('data-status') === filter) {
                        item.style.display = '';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // Lazy loading des images
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        imageObserver.observe(img);
    });

    // Gestion des tooltips Bootstrap
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(tooltip => {
        new bootstrap.Tooltip(tooltip);
    });

    // Gestion des modales Bootstrap
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('shown.bs.modal', function() {
            const autofocus = modal.querySelector('[autofocus]');
            if (autofocus) {
                autofocus.focus();
            }
        });
    });

    // Smooth scroll pour les liens d'ancrage
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                e.preventDefault();
                const offsetTop = targetElement.offsetTop - 80; // Hauteur de la navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Gestion du préloader (si présent)
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', function() {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500);
        });
    }

    // Animation d'écriture pour le titre (effet typewriter)
    const typewriterElement = document.querySelector('.typewriter');
    if (typewriterElement) {
        const text = typewriterElement.textContent;
        typewriterElement.textContent = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                typewriterElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        setTimeout(typeWriter, 1000);
    }

    // Gestion des alertes auto-dismiss
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (alert.classList.contains('alert-success')) {
            setTimeout(() => {
                alert.style.opacity = '0';
                setTimeout(() => {
                    alert.remove();
                }, 300);
            }, 5000);
        }
    });

    // Fonction utilitaire pour débouncer les événements
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Optimisation du scroll avec debounce
    const debouncedScroll = debounce(function() {
        // Actions à exécuter lors du scroll
        console.log('Scroll optimisé');
    }, 100);

    window.addEventListener('scroll', debouncedScroll);

    // Gestion des erreurs JavaScript
    window.addEventListener('error', function(e) {
        console.error('Erreur JavaScript:', e.error);
        // Optionnel: envoyer l'erreur à un service de monitoring
    });

    // Fonction pour copier du texte dans le presse-papiers
    window.copyToClipboard = function(text) {
        navigator.clipboard.writeText(text).then(function() {
            // Afficher une notification de succès
            showToast('Copié dans le presse-papiers!', 'success');
        }).catch(function(err) {
            console.error('Erreur lors de la copie:', err);
            showToast('Erreur lors de la copie', 'error');
        });
    };

    // Fonction pour afficher des notifications toast
    window.showToast = function(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        const toastContainer = document.querySelector('.toast-container') || createToastContainer();
        toastContainer.appendChild(toast);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    };

    // Créer un conteneur pour les toasts s'il n'existe pas
    function createToastContainer() {
        const container = document.createElement('div');
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1055';
        document.body.appendChild(container);
        return container;
    }
});

// Fonction globale pour rafraîchir les animations AOS
window.refreshAOS = function() {
    if (typeof AOS !== 'undefined') {
        AOS.refresh();
    }
};