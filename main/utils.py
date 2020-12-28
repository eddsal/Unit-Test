from main.models import *


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
                    print('you re`age is {}. you must have at least 13 years old'.format(i))
                    return False
                # else:
                #     return True
            if i == 'password' and len(dictt[i]) < 8 or len(dictt[i]) > 40:
                print("you're password must be betwwen 8 and 40 charcater ")
                return False
    return True


def canCreateList(email):
    if email:
        if len(List.objects.filter(useraccount=UserAccount.objects.filter(email=email).first())) == 1:
            print('cannot create a list, already have a list')
            return False
    return True
