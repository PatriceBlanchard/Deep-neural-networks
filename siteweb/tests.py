# Create your tests here.

from django.test import TestCase
from siteweb.models import PostCategory, Post
from django.utils import timezone
from django.urls import reverse
from .forms import ContactForm
from siteweb import views
from django.conf import settings
import requests

class sitewebdnnTest(TestCase):

    def setUp(self):
        # Création d'une catégorie et d'un post
        self.cat = PostCategory.objects.create(name='Test')

        self.post = Post.objects.create(
            title=b'Deep Learning - Posts',
            category=self.cat,
            published=True,
            text="only a test",
            created_at=timezone.now())

    def test_postcategory_creation(self):
        # Test de la catégorie d'un post
        self.assertTrue(isinstance(self.cat, PostCategory))
        self.assertEqual(self.cat.__str__(), self.cat.name)

    def test_post_creation(self):
        # Test d'un post
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_views_accueil(self):
        # Test du retour de la page accueil.html
        url = reverse(views.accueil)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_chronologie(self):
        # Test du retour de la page chronologie.html
        url = reverse(views.chronologie)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_cnn(self):
        # Test du retour de la page cnn.html
        url = reverse(views.cnn)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_rnn(self):
        # Test du retour de la page rnn.html
        url = reverse(views.rnn)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_post_list(self):
        # Test du retour de la page post_list.html
        url = reverse(views.post_list)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.post.title, resp.content)

    def test_views_post_detail(self):
        # Test du retour de la page post_detail.html
        url = reverse(views.post_detail, kwargs={'post_id': '1'})
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.post.title, resp.content)

    def test_views_image(self):
        # Test du retour de la page application_image.html
        url = reverse(views.image)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_predictImage(self):
        # Test du retour de la prédiction d'une image envoyée à l'API
        testimage = './static-res/img/image_classification/Y25.jpg'
        upload = {
            'picture': open(testimage, 'rb')
        }

        api = settings.URL_TUMOR_API
            #'http://188.166.6.223/api/upload/xray'
        response = requests.post(api, files=upload)
        self.assertEqual(response.status_code, 201)

    def test_views_texte(self):
        # Test du retour de la page application_texte.html
        url = reverse(views.texte)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_video(self):
        # Test du retour de la page application_video.html
        url = reverse(views.video)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_audio(self):
        # Test du retour de la page application_audio.html
        url = reverse(views.audio)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_about(self):
        # Test du retour de la page about.html
        url = reverse(views.about)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_views_contact(self):
        # Test du retour de la page contact.html
        url = reverse(views.contact)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_valid_form(self):
        # Test du formulaire
        data = {'from_email': 'contact@test.fr',
                'subject': 'test',
                'message': 'test'
                }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
