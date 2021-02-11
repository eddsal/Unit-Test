

# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from main.models import UserAccount
from main.utils import random_char




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
        response = self.client.post('/user/add', {'email':email , 'age': '13', 'firstName': 'e', 'lastName': 'e', 'password': 'eeeeeeeeeeeeee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserAccount.objects.get(email=email))
    
    def test_d_create_invalid_user(self):
        """
        creation d utilisateur Invalid.
        """
        email = "Admiaadsn@test.com"
        response = self.client.post('/user/add', {'email':email , 'age': '1', 'firstName': 'e', 'lastName': 'e', 'password': 'eeeeeeeeeeeeee'})
        self.assertEqual(response.status_code, 400)

    
    def test_e_create_list(self):
        """
        creation d'une liste.
        """
        validUser = UserAccount.objects.create(email="{}valid2@test.com".format(random_char(5)), age="23")
        response = self.client.post('/user/add/list', {'email':   validUser.email, 'listt':'',  'age': '15'})
        self.assertEqual(response.status_code, 200)


    def test_get_e_user_list(self):
        """
        Get USER Liste.
        """
        validUser, created = UserAccount.objects.get_or_create(email="valid@test.com")
        response = self.client.post('/user/{}/get/list'.format(validUser.id))
        self.assertEqual(response.status_code, 200)

    
    def test_get_e_user_Items(self):
        """
        Get USER ITEMS FROM  Liste.
        """
        validUser, created = UserAccount.objects.get_or_create(email="valid@test.com")
        response = self.client.post('/user/{}/get/list/items/'.format(validUser.id))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
