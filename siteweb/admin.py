from django.contrib import admin
from django.forms import Textarea
from django.db import models
from siteweb.models import PostCategory, Post

# Le fichier admin.py assure la configuration de l'interface de gestion des modèles de données.

# Cette interface génère automatiquement est une sorte de mini-site web intégré au projet qui permet de réaliser
# des opérations CRUD (Create, Read,Update, Delete) sur les données des tables de base de données.
# L'accès à ce mini-site se réalise après avoir définit un login et un mot de passe via la
# commande ./manage.py createsuperuser

# Personnalisation de l'interface :

@admin.register(PostCategory)
# Décorateur pour l'enregistrement de la classe PostCategory de type ModelAdmin
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    # personnalisation du champs de recherche par nom

@admin.register(Post)
# Décorateur pour l'enregistrement de la classe Post de type ModelAdmin
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'published',
        'created_at',
    )
    # L'ensemble des sections qui sera affichées pour présenter un post à l'adresse ../admin/siteweb/post :

    list_filter = (
        'category__name',
        'published',
    )
    # L'ensemble des filtres mit à disposition dans cette interface

    autocomplete_fields = ['category']
    # Définir l'autocomplétion de la catégorie sur le champ name
    # Cette variable est associée à la variable search_fields dans la classe PostCategoryAdmin

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 90})}
    }
    # Surcharge dans le but d'agrandir le Textarea lors de la création d'un post
