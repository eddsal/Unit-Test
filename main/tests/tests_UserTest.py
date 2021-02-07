

# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse



class ApiTestCase(TestCase):
    def test_index_loads_properly(self):
            """The index page loads properly"""
            response = self.client.get('http://127.0.0.1:8000/')
            self.assertEqual(response.status_code, 200)
 
    def test_user(self):
        """
        Affichage de la page d'accueil : liste des articles.
        """
        print('ds ')
        response = self.client.get(reverse('main:createValidUser'))
        # self.failUnless(isinstance(response.context['articles'], QuerySet))
        print(response.status_code)
        self.failUnlessEqual(response.status_code, 200)