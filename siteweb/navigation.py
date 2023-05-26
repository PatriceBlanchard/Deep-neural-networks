from django.urls import reverse_lazy

# Les sections affichées dans la barre de navigation
NAV_ACCUEIL = 'Accueil'
NAV_CHRONOLOGIE = 'Chronologie'
NAV_CNN = 'CNN'
NAV_RNN = 'RNN'
NAV_POSTS = 'Blog'
NAV_IMAGE = 'Image'
NAV_TEXTE = 'Texte'
NAV_VIDEO = 'Video'
NAV_AUDIO = 'Audio'
NAV_ABOUT = 'À propos'
NAV_CONTACT = 'Contact'

# Les items de la barre de navigation
NAV_ITEMS = (
    (NAV_ACCUEIL, reverse_lazy('accueil')),
    # reverse_lazy récupère l'URL de 'accueil'
    (NAV_CHRONOLOGIE, reverse_lazy('chronologie')),
    (NAV_CNN, reverse_lazy('cnn')),
    (NAV_RNN, reverse_lazy('rnn')),
    (NAV_POSTS, reverse_lazy('home')),
    (NAV_ABOUT, reverse_lazy('about')),
    (NAV_CONTACT, reverse_lazy('contact')),
    # Application : image, vidéo et texte sont intégrés dans le fichier base.html
    # à partir de la ligne 35
)

def navigation_items(selected_item):
    # Renvoie les items de la barre de navigation
    items = []
    for name, url in NAV_ITEMS:
        items.append({
            'name': name,
            # Le nom d'une section de la barre de navigation
            'url': url,
            # Son url
            'active': True if selected_item == name else False
            # Activer la mise en surbrillance de l'item sélectionné dans la barre de navigation
        })
    return items
    # Retourner la variable items