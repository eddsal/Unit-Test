from main.models import *
import random
import string
from datetime import datetime


"""
this function  will return a bool with some infos about the recieved data.
"""


def isValid(dictt):
    for i in dictt:
        if dictt[i] is None or dictt[i] == '':
            print('no value has been set to', i)
            return False
        else:
            if i == 'age':
                if(int(str(dictt[i])) == '' or int(str(dictt[i])) < 13):
                    print('you re`age is {}. you must have at least 13 years old'.format(dictt[i]))
                    return False
                # else:
                #     return True
            if i == 'password' and len(dictt[i]) < 8 or len(dictt[i]) > 40:
                print("you're password must be betwwen 8 and 40 charcater ")
                return False
    return True


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def canCreateList(email):
    if email:
        if len(List.objects.filter(useraccount=UserAccount.objects.filter(email=email).first())) == 1:
            print('cannot create a list for {}, already have a list'.format(email))
            return False
    return True


def add(items):
    maxItem = 11
    count = 0
    db_items = Items.objects.filter(list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user']))).count()
    # last_added_item = Items.objects.get(list_to_do=List.objects.get(
    #     useraccount=UserAccount.objects.get(email=items['user'])))

    if items:
        for item in items:
            if item == 'name' and Items.objects.filter(name=items[item]).exists():
                print('item containing the name {} already exist'.format(items[item]))
                return False
            if item == 'content':
                if len(items[item]) > 1000:
                    print('max lenght of the content is 1000 charachters. u wrote {}'.format(len(items[item])))
                    return False
    if db_items > 1:
        db_items = db_items + 1
        def impaire(x, y): return [n for n in range(db_items, (10 + 1)) if n % 2]
        array = impaire(db_items, 10)
        date = Items.objects.filter(list_to_do=List.objects.get(
            useraccount=UserAccount.objects.get(email=items['user']))).last().created
        now = datetime.now()
        if (len(array) == 4):
            if int(date.strftime("%M")) - 30 > int(now.strftime("%M")):
                return True
            else:
                print('u created two items in less thn 30 mins')
                return False
        elif (len(array) == 3):
            if int(date.strftime("%M")) - 30 > int(now.strftime("%M")):
                return True
            else:
                print('u created two items in less thn 30 mins')
                return False
        elif (len(array) == 2):
            if int(date.strftime("%M")) - 30 > int(now.strftime("%M")):
                return True
            else:
                print('u created two items in less thn 30 mins')
                return False
        elif (len(array) == 1):
            if int(date.strftime("%M")) - 30 > int(now.strftime("%M")):
                return True
            else:
                print('u created two items in less thn 30 mins')
                return False

        print(array)

        count + 1
    if db_items - maxItem == 0:
        print('max items in your e list have been reached ')
        return False

    if count == 2:
        print('3arsa', )

    # # db_items + 1
    # if db_items:

    #     count += 1
    #     if count == 2:
    #         # if

    #         print('max item creation has been acceded try in few minutes')

    #         return False

    return True
