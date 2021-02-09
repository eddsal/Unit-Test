

# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from main.models import UserAccount




class ApiTestCase(TestCase):
   
    def setUp(self):
        self.user = UserAccount.objects.create(email="Admidsn@test.com",age=42)

    def test_a_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')

    def test_b_user(self):
        """
        Affichage de la page de creation d utilisateru.
        """
        response = self.client.get(reverse('main:createValidUser'))
        self.failUnlessEqual(response.status_code, 200)


    def test_c_create_user(self):
        """
        creation d utilisateur.
        """
        email = "Admivdsn@test.com"
        response = self.client.post('/create/user', {'email':email , 'age': '13', 'firstName': 'e', 'lastName': 'e', 'password': 'eeeeeeeeeeeeee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserAccount.objects.get(email=email))
    
    def test_d_create_invalid_user(self):
        """
        creation d utilisateur.
        """
        email = "Admiaadsn@test.com"
        response = self.client.post('/create/user', {'email':email , 'age': '1', 'firstName': 'e', 'lastName': 'e', 'password': 'eeeeeeeeeeeeee'})
        self.assertEqual(response.status_code, 400)

    
    # def test_e_create_list(self):
    #     """
    #     creation d'une liste.
    #     """
    #     response = self.client.post('/create/list', {'email':    self.user.email})
    #     self.assertEqual(response.status_code, 200)

