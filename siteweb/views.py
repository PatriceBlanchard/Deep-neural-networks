from django.shortcuts import get_object_or_404
from siteweb.models import Post
from siteweb import model_helpers
from siteweb import navigation
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

import requests
import urllib
import json

# Le fichier views.py contient les fonctions générant les réponses HTTP à renvoyer au navigateur de l'utilisateur
# La liste des fonctions qui seront appelées par le module de routing (définit dans le fichier urls.py)

def accueil(request):
    # La fonction associée à la rubrique accueil de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_ACCUEIL),
    }

    return render(request, 'site/accueil.html', context)
    # Retourne le contexte et l'emplacement du fichier accueil.html


def chronologie(request):
    # La fonction associée à la rubrique chronologie de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CHRONOLOGIE),
    }

    return render(request, 'site/chronologie.html', context)
    # Retourne le contexte et l'emplacement du fichier chronologie.html

def cnn(request):
    # La fonction associée à la rubrique cnn de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CNN),
    }

    return render(request, 'site/cnn.html', context)
    # retourne le contexte et l'emplacement du fichier cnn.html

def rnn(request):
    # La fonction associée à la rubrique rnn de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_RNN),
    }

    return render(request, 'site/rnn.html', context)
    # Retourne le contexte et l'emplacement du fichier rnn.html


def post_list(request, category_name=model_helpers.post_category_all.slug()):
    # La fonction associée à la rubrique blog de la barre de navigation et dédiée à l'affichage de l'ensemble des posts
    category, posts = model_helpers.get_category_and_posts(category_name)
    # récupère la catégorie et les posts à afficher suivant leur sélection par l'utilisateur
    categories = model_helpers.get_categories()
    # Récupère les catégories à afficher sur la partie droite du blog

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        # L'objet Blog de la barre de navigation
        'category': category,
        # La catégorie
        'posts': posts,
        # Le ou les pots
        'categories': categories,
        # L'ensemble des catégories à afficher pour sélection
    }

    return render(request, 'site/post_list.html', context)
    # Retourne le contexte et l'emplacement du fichier post_list.html

def post_detail(request, post_id):
    # La fonction associée à la rubrique blog de la barre de navigation et dédiée à l'affichage d'un seul post
    post = get_object_or_404(Post, pk=post_id)
    # Récupérer le post ou une erreur à partir de son identifiant dans la table de base de données Post
    posts_same_category = Post.objects.filter(published=True, category=post.category) \
        .exclude(pk=post_id)
    # Récupérer les posts publiés d'une même catégorie

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        # L'objet Blog de la barre de navigation
        'post': post,
        # Le post
        'posts_same_category': posts_same_category,
        # Les posts de même catégories

    }

    return render(request, 'site/post_detail.html', context)
    # Retourne le contexte et l'emplacement du fichier post_detail.html


def image(request):
    # La fonction associée à la rubrique Application Image de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_IMAGE),
        # L'objet Image de la barre de navigation
    }

    return render(request, 'site/application_image.html', context)
    # Retourne le contexte et l'emplacement du fichier application_image.html


def predictImage(request):
    # La fonction associée à la rubrique Application Image de la barre de navigation assurant la prédiction d'une image
    fileobj = request.FILES['filePath']
    # Recupérer l'emplacement de l'image
    #print("fileobj")
    #print(fileobj)
    fs = FileSystemStorage()
    filePathName = fs.save(fileobj.name, fileobj)
    # Enregistrer l'image dans le dossier media du serveur web
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName
    #print("testimage")
    #print(testimage)
    api = settings.URL_TUMOR_API
    upload = {
        'picture': open(testimage, 'rb')
    }
    response = requests.post(api, files=upload)
    # Envoyer l'image à l'API
    data = response.json()
    # Réponse de l'API proposant les résultats de la prédiction


    context = {
        'vgg_prediction': data['vgg_tumor_pred'],
        # Le résultat de la prédiction du modèle VGG
        'resnet_prediction': data['resnet_tumor_pred'],
        # Le résultat de la prédiction du modèle resnet
        'inception_resnet_v2_prediction': data['inception_resnet_v2_tumor_pred'],
        # Le résultat de la prédiction du modèle inception resnet V2
        'navigation_items': navigation.navigation_items(navigation.NAV_IMAGE),
        # L'objet Image de la barre de navigation
    }
    return render(request, 'site/application_image.html', context)
    # Retourne le contexte et l'emplacement du fichier application_image.html


def texte(request):
    # La fonction associée à la rubrique Application Texte de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_TEXTE),
    }
    # L'objet Texte de la barre de navigation

    return render(request, 'site/application_texte.html', context)
    # retourne le contexte et l'emplacement du fichier application_texte.html

def video(request):
    # La fonction associée à la rubrique Application Vidéo de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_VIDEO),
    }
    # L'objet Vidéo de la barre de navigation

    return render(request, 'site/application_video.html', context)
    # Retourne le contexte et l'emplacement du fichier application_video.html


def audio(request):
    # La fonction associée à la rubrique Application Audio de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_AUDIO),
    }
    # L'objet audio de la barre de navigation

    return render(request, 'site/application_audio.html', context)
    # Retourne le contexte et l'emplacement du fichier application_audio.html


def about(request):
    # La fonction associée à la rubrique À Propos de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_ABOUT),
    }
    # Lo'bjet about de la barre de navigation

    return render(request, 'site/about.html', context)
    # Retourne le contexte et l'emplacement du fichier about.html


def contact(request):
    # La fonction associée à la rubrique À Propos de la barre de navigation
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_CONTACT),
        # L'objet Contact de la barre de navigation
    }
    if request.method == 'POST':
        # Si la méthode est de type POST
        form = ContactForm(request.POST)
        # récupérer l'objet form
        if form.is_valid():
            # si l'objet est valide
            from_email = form.cleaned_data['from_email']
            # Récupérer l'e-mail d'envoi
            subject = form.cleaned_data['subject']
            # Récupérer le sujet du mail
            message = form.cleaned_data['message']
            # Récupérer le message du mail
            message = "De : " + str(from_email) + " - " + str(message)
            # Ajouter l'adresse du mail de l'émetteur dans le mail reçu par l'administration
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            # Retour du recaptcha
            url = settings.URL_GOOGLE_API
            # Enregistrer dans la variable url, l'adresse de l'API Google du recaptcha
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                # La clé secrète
                'response': recaptcha_response
                # la réponse
            }
            data = urllib.parse.urlencode(values).encode()
            # urllib.parse.urlencode convertir le dictionnaire value en chaîne de requête.
            req = urllib.request.Request(url, data=data)
            # Envoi de la requète à l'API Google
            response = urllib.request.urlopen(req)
            # retour de la réponse
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            # Résultat de la réponse
            if result['success']:
                # le résultat est correct
                try:
                    send_mail(subject, message, from_email, ['patriceblanchard.perso@gmail.com'])
                    # Le sujet, le mail et le mail est envoyé à l'adresse mail 'patriceblanchard.perso@gmail.com'
                except BadHeaderError:
                    return render(request, "site/contact_error.html", context)
                    # en cas d'erreur, la page contact_error le signale
                return render(request, "site/contact_success.html", context)
                # en cas de réussite, la page contact_success spécifie que le mail a bien été envoyé
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                # sinon le recaptcha présente un problème
                form = ContactForm()
                # un nouveau formulaire est chargée

                context['form'] = form

    return render(request, "site/contact.html", context)
    # Retourne le contexte et l'emplacement du fichier about.html