

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
        Affichage de la page de creation d utilisateru.
        """
        response = self.client.get(reverse('main:createValidUser'))
        self.failUnlessEqual(response.status_code, 200)

    def test_create_user(self):
        """
        creation d utilisateur.
        """
        response = self.client.post('/create/user', {'email': "Admidsn@test.com", 'age': '13', 'firstName': 'e', 'lastName': 'e', 'password': 'eeeeeeeeeeeeee'})
        self.assertEqual(response.status_code, 200)