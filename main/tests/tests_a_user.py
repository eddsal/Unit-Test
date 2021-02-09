# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from main.models import UserAccount
from main.models import *
from main.utils import isValid, random_char
import unittest


class LoginViewTest(unittest.TestCase):
    
    def setUp(self):
        self.user = UserAccount.objects.get_or_create(email="valid@test.com", age=42, first_name='e', last_name='e', password='eeeeeeeeeeeeee')

    def test_create_valid_user(self):
        print('function: test_create_valid_user')
        data = {'email': random_char(3)+"Admin@test.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertTrue(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_without_age(self):
        print('function: test_create_user_without_age')
        data = {'email':  random_char(7)+"@gmail.com", 'age': '', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_without_first_name(self):
        print('function: test_create_user_without_first_name')
        data = {'email':  random_char(7)+"@gmail.com", 'age': '13', 'first_name': '', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_without_last_name(self):
        print('function: test_create_user_without_last_name')
        data = {'email':  random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': '', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_without_email(self):
        print('function: test_create_user_without_email')
        data = {'email': '', 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_without_password(self):
        print('function: test_create_user_without_password')
        data = {'email':  random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': ''}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_with_false_age(self):
        print('function: test_create_user_with_false_age')
        data = {'email':  random_char(7)+"@gmail.com", 'age': '12', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_with_false_email(self):
        print('function: test_create_user_with_false_email')
        data = {'email': random_char(7) + ".com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

    def test_create_user_false_password(self):
        print('function: test_create_user_false_password')
        data = {'email': random_char(7) + "@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eee'}
        self.assertFalse(isValid(data) == True)
        print('----------------------------')
        print('')

if __name__ == '__main__':
    unittest.main()
