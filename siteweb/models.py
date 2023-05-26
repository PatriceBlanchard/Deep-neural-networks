from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Ce fichier gère la création de modèles de données via une classe de représentation des données que l'on souhaite
# manipuler et stocker dans une base de données. Une classe assure ainsi l'ajout et la synchronisation
# des tables de base données.

# Un modèle = une classe = une table
# chaque attribut d'une classe représente une colonne d'une table

class PostCategory(models.Model):
    # La classe Postcategory héritant de models.Model
    name = models.CharField(max_length=50)
    # PostCategory est uniquement défini par un nom

    # slugify() transforme une catégorie en URL valide en remplaçant les espaces par un tiret
    # ainsi que les majuscules en minuscules
    def slug(self):
        return slugify(self.name)

    def __str__(self):
        # Surcharge de la méthode __str__
        return self.name
        # retourne le nom de la catégorie

class Post(models.Model):
    # La classe Posts héritant de models.Model
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory',
    # Une clé étrangère vers PostCategory, suivi de la configuration possible :
                                 null=True,
                                 # Autorise le fait d'avoir une valeur nulle
                                 blank=True,
                                 # Autorise le fait d'avoir une chaîne vide
                                 on_delete=models.DO_NOTHING)
                                 # Lors de la suppression ne rien faire

    published = models.BooleanField(default=False)
    # le statu publié ou non du post, sachant que par défaut un post n'est pas publié (default = False)
    text = RichTextUploadingField()
    #  La mise en forme de la partie message du post est enrichie à l'aide du package ckeditor
    created_at = models.DateTimeField(auto_now_add=True)
    # Enregistrement de la date de création du post

    def __str__(self):
        return self.title
        # Retourne le titre