# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
# from unittest.mock import patch
from main.models import *
from main.utils import isValid
import unittest
import random
import string


class LoginViewTest(unittest.TestCase):

    def random_char(self, y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    def test_create_valid_user(self):
        print('function: test_create_valid_user')
        data = {'email': self.random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
            self.assertTrue(data['email'] == UserAccount.objects.last().email)
            self.assertTrue(int(data['age']) >= 13)
        print('----------------------------')
        print('')

    def test_create_user_without_age(self):
        print('function: test_create_user_without_age')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['age']) == 0)
        print('----------------------------')
        print('')

    def test_create_user_without_first_name(self):
        print('function: test_create_user_without_first_name')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '13', 'first_name': '', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):

            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['first_name']) == 0)
        print('----------------------------')
        print('')

    def test_create_user_without_last_name(self):
        print('function: test_create_user_without_last_name')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': '', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['last_name']) == 0)
        print('----------------------------')
        print('')

    def test_create_user_without_email(self):
        print('function: test_create_user_without_email')
        data = {'email': '', 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['email']) == 0)
        print('----------------------------')
        print('')

    def test_create_user_without_password(self):
        print('function: test_create_user_without_password')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': ''}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['password']) == 0)
        print('----------------------------')
        print('')

    def test_create_user_with_false_age(self):
        print('function: test_create_user_with_false_age')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '12', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['age']) < 13)
        print('----------------------------')
        print('')

    def test_create_user_with_false_email(self):
        print('function: test_create_user_with_false_email')
        data = {'email':  self.random_char(7)+".com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eeeeeeeeeeeeee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        print('----------------------------')
        print('')

    def test_create_user_false_password(self):
        print('function: test_create_user_false_password')
        data = {'email':  self.random_char(7)+"@gmail.com", 'age': '13', 'first_name': 'e', 'last_name': 'e', 'password': 'eee'}
        if (isValid(data)):
            print('User is Valid')
            UserAccount.objects.create(email=data['email'], age=data['age'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
        else:
            self.assertTrue(len(data['password']) < 8 or len(data['password']) > 40)
        print('----------------------------')
        print('')


if __name__ == '__main__':
    unittest.main()
