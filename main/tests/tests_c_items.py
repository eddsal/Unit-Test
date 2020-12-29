# from django.contrib.auth import get_user_model
from django.test import Client, TestCase
# from unittest.mock import patch
from main.models import *
import unittest
from main.utils import add, random_char


class ItemsViewTest(unittest.TestCase):

    def test_create_item(self):
        print('function: test_create_item')
        items = {'name': random_char(5), 'content': 'dsd', 'user': UserAccount.objects.first().email}
        if (add(items)):
            self.true = add(items)
            Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
                useraccount=UserAccount.objects.get(email=UserAccount.objects.first().email)))
            print('Item name :{} created'.format(items['name']))
            self.assertTrue(self.true == True)

        print('----------------------------')
        print('')

    def test_create_item_with_same_name(self):
        print('function: test_create_item_with_same_name')
        allItems = Items.objects.filter(list_to_do=List.objects.get(
            useraccount=UserAccount.objects.get(email=UserAccount.objects.first().email)))
        items = {'name': allItems.last().name, 'content': '', 'user': UserAccount.objects.first().email}

        if add(items):
            Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
                useraccount=UserAccount.objects.get(email=UserAccount.objects.first().email)))
        else:
            self.false = add(items)
        self.assertFalse(self.false == True)

    # def test_create_many_items(self):
    #     print('function: test_create_many_items')
    #     print(List.objects.get(
    #         useraccount=UserAccount.objects.get(email=UserAccount.objects.first().email)))

    # print(Items.objects.filter(list_to_do=List.objects.get(
    #     useraccount=UserAccount.objects.get(email=UserAccount.objects.first().email))))
    # allItems=Items.objects.filter(list_to_do=[v for v in List.objects.filter(
    #     useraccount=UserAccount.objects.filter(email=UserAccount.objects.last().email).first())][0])
    # items={'name': allItems[0].name, 'content': '', 'user': UserAccount.objects.last().email}

    # if add(items):
    #     print(add(items))
    #     Items.objects.create(name=items['name'], content=items['content'], list_to_do=[v for v in List.objects.filter(
    #         useraccount=UserAccount.objects.filter(email=items['user']).first())][0])

    # items = {'name': 'edd', 'content': 'dsd'}
    # if (add(items)):
    #     Items.objects.create(name=items['name'], content=items['content'], list_to_do=[v for v in List.objects.filter(
    #         useraccount=UserAccount.objects.filter(email='Admin@test.com').first())][0])
    #     print('creating name')
    # print('----------------------------')
    # print('')
if __name__ == '__main__':
    unittest.main()
