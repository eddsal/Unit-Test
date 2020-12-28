# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
# from unittest.mock import patch
from main.models import *
import unittest
from main.utils import canCreateList


class ListViewTest(unittest.TestCase):

    def test_create_more_thn_one_list(self):
        print('function: test_create_more_thn_one_list')
        if (canCreateList('HaAAuKA@gmail.com')):
            user = UserAccount.objects.get(email='HaAAuKA@gmail.com')
            user.listt = List.objects.create(name="TODILIST")
            user.save()
        else:
            self.assertTrue(len(List.objects.filter(useraccount=UserAccount.objects.filter(email='HaAAuKA@gmail.com').first())) == 1)
        print('----------------------------')
        print('')

    def test_create_list(self):
        print('function: test_create_list')
        if (canCreateList(UserAccount.objects.last().email)):
            user = UserAccount.objects.get(email=UserAccount.objects.last().email)
            user.listt = List.objects.create(name="TODILIST")
            user.save()
            print('TODOLIST created for {}'.format(UserAccount.objects.last().email))
        else:
            self.assertTrue(len(List.objects.filter(useraccount=UserAccount.objects.filter(email='HaAAuKA@gmail.com').first())) == 1)
        print('----------------------------')
        print('')


if __name__ == '__main__':
    unittest.main()
