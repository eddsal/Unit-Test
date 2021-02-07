# # from django.contrib.auth import get_user_model
# from django.test import Client, TestCase
# # from unittest.mock import patch
# from main.models import *
# import unittest
# from main.utils import canCreateList
# import random
# import string


# class ListViewTest(unittest.TestCase):

#     def test_create_more_thn_one_list(self):
#         print('function: test_create_more_thn_one_list')
#         if (canCreateList(UserAccount.objects.first().email)):
#             user = UserAccount.objects.get(email=UserAccount.objects.first().email)
#             user.listt = List.objects.create(name="TODILIST")
#             user.save()
#         else:
#             self.assertFalse(len(List.objects.filter(useraccount=UserAccount.objects.filter(email=UserAccount.objects.first().email).first())) == 2)
#         print('----------------------------')
#         print('')

#     def test_create_list(self):
#         print('function: test_create_list')
#         if (canCreateList(UserAccount.objects.first().email)):
#             user = UserAccount.objects.get(email=UserAccount.objects.first().email)
#             user.listt = List.objects.create(name="TODILIST")
#             user.save()
#             print('TODOLIST created for {}'.format(UserAccount.objects.first().email))
#         else:
#             self.assertTrue(len(List.objects.filter(useraccount=UserAccount.objects.filter(email=UserAccount.objects.first().email).first())) == 1)
#         print('----------------------------')
#         print('')


# if __name__ == '__main__':
#     unittest.main()
