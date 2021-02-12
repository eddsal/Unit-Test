from main.models import *
import random
import string
import datetime


"""
this function will check if the user we are trying to create is valid
@param1 = {}
return True or False
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
            if i == 'email':
                if '@' not in dictt[i]:
                    print("Invalid Email")
                    return False
    return True


"""
this function will generate random char
@param1 = int
return str
"""


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


"""
this function will return a bool if a user can have + 1 list
@param1 = email
return bool
"""


def canCreateList(user):
    if user:
        if len(List.objects.filter(useraccount=UserAccount.objects.get(email=user.email))) and  len(List.objects.filter(useraccount=UserAccount.objects.get(email=user.email)))== 1:
            print('cannot create a list for {}, already have a list'.format(user.email))
            return False
        else:
            user.listt=List.objects.create(name="TODILIST")
            user.save()
            print('A list for {}, already have a list'.format(user.email))
            
            
    return True

"""
this function will return a bool if a user can create items

@param1 = items
return bool
"""
def add(items):
    
    maxItem = 11
    db_items = Items.objects.filter(list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user']))).count()  # geeting all the users 'list items
    if items:
        for item in items:
            if item == 'name' and Items.objects.filter(name=items[item]).exists():  # checking if an item with this name already exist
                print('item containing the name {} already exist'.format(items[item]))
                return False
            if item == 'content':
                if len(items[item]) > 1000:  # checking  content len
                    print('max lenght of the content is 1000 charachters. u wrote {}'.format(len(items[item])))
                    return False
      

    if db_items > 1:
        """
        getting the last created item date
        """
        date = Items.objects.filter(list_to_do=List.objects.get(
            useraccount=UserAccount.objects.get(email=items['user']))).last().created
        created_date = date.strftime('%Y-%m-%d %H:%M:%S').replace(':', ' ').split('-')
        timer = ' '.join(created_date).split(' ')
        lst = []
        for intt in timer:
            intt = int(intt)
            lst.append(intt)

        '''subctracing  current date with the lasdt createf item date'''
        date_minutes = datetime.datetime.now() - datetime.datetime(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5])
        minutes = divmod(date_minutes.total_seconds(), 60)
        # now = datetime.now()

        if (db_items == 2):
            if minutes[0] > 30:
                Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user'])))
                return True
            else:
                print('u created two items in less thn 30 mins, you have to wait {} more minutes'.format(30 - minutes[0]))
                return False
        elif (db_items == 4):
            if minutes[0] > 30:
                Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user'])))
                return True
            else:
                print('u created two items in less thn 30 mins, you have to wait {} more minutes'.format(30 - minutes[0]))
                return False
        elif (db_items == 6):

            if minutes[0] > 30:
                Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user'])))
                return True
            else:
                print('u created two items in less thn 30 mins, you have to wait {} more minutes'.format(30 - minutes[0]))
                return False
        elif (db_items == 8):
            if minutes[0] > 30:
                Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user'])))
                return True
            else:
                print('u created two items in less thn 30 mins, you have to wait {} more minutes'.format(30 - minutes[0]))
                return False
    
    Items.objects.create(name=items['name'], content=items['content'], list_to_do=List.objects.get(
        useraccount=UserAccount.objects.get(email=items['user'])))
 
    
    if db_items - maxItem == 0:
        print('max items in your e list have been reached ')
        return False

    if db_items == 8:
        print('you only can  add 2 more items ')
    return True
