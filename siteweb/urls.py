from django.urls import path

from siteweb import views
from django.conf.urls.static import static
from django.conf import settings

# Gestion du routing décidant quelle fonction va traiter telle requête HTTP.

# Règles de matching intégré dans la variable urlpatterns
urlpatterns = [
    path('', views.accueil, name='index'),
    path('accueil/', views.accueil, name='accueil'),
    path('chronologie/', views.chronologie, name='chronologie'),
    path('cnn/', views.cnn, name='cnn'),
    path('rnn/', views.rnn, name='rnn'),
    path('image/', views.image, name='image'),
    path('image/predictImage', views.predictImage, name='predictImage'),
    path('texte/', views.texte, name='texte'),
    path('video/', views.video, name='video'),
    path('audio/', views.audio, name='audio'),

    # URLs de gestion du Blog
    path('posts/', views.post_list, name='home'),
    path('posts/<str:category_name>/', views.post_list, name='post-list'),
    path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
# Ajout de l'emplacement du dossier MEDIA, un dossier où seront enregistrés des images envoyées par l'utilisateur
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)