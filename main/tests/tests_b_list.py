# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
# from unittest.mock import patch
from main.models import *
import unittest
from main.utils import canCreateList, random_char
import random
import string


class ListViewTest(unittest.TestCase):

    def setUp(self):
        self.user = UserAccount.objects.get(email="valid@test.com")
        if  not self.user.listt:
            self.user.listt = List.objects.create(name="TODILIST")
            self.user.save()


    def test_create_more_thn_one_list(self):
        print('function: test_create_more_thn_one_list')
        self.assertFalse(canCreateList(self.user) == True)
        print('----------------------------')
        print('')

    def test_create_list(self):
        
        print('function: test_create_list')
        validUser, created = UserAccount.objects.get_or_create(email="{}valid2@test.com".format(random_char(5)), age="23")
        self.assertTrue(canCreateList(validUser)  == True)
        print('----------------------------')
        print('')


if __name__ == '__main__':
    unittest.main()
