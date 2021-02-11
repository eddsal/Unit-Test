# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from main.models import *
import unittest
from main.utils import add, random_char


class ItemsViewTest(unittest.TestCase):
    def setUp(self):
        self.user = UserAccount.objects.get(email="valid@test.com")
        
        
    def test_a_create_item(self):
        print('function: test_create_item')
        items = {'name': random_char(5), 'content': 'dsd', 'user':   self.user.email}
        print('Item name :{} created'.format(items['name']))
        self.assertTrue(add(items)== True)
        print('----------------------------')
        print('')

    def test_create_item_with_same_name(self):
        print('function: test_create_item_with_same_name')
        allItems = Items.objects.filter(list_to_do=List.objects.get(
                    useraccount=UserAccount.objects.get(email=self.user.email)))
        items = {'name': allItems.last().name, 'content': '', 'user': self.user.email}
        self.assertFalse(add(items) == True)
        print('----------------------------')
        print('')

    def test_wait_30mins(self):
        print('function: test_30mins_wait')
        allItems = Items.objects.filter(list_to_do=List.objects.get(
                    useraccount=UserAccount.objects.get(email=self.user.email)))
        items = {'name': random_char(6), 'content': 'test', 'user': self.user.email}
        self.assertTrue(add(items) == False)
        print('----------------------------')
        print('')
       

if __name__ == '__main__':
    unittest.main()
