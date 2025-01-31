from typing import List


def ReguisterUser(user_info:List[dict],user_name,password):
    if user_info.count({'user_name':user_name,'password':password}) > 0:
        print('user is already registered')
    else:
        user_info.append({'user_name':user_name,'password':password})
        print('user registered successfully')


def LoginUser(user_info:List[dict],user_name,password):
    if user_info.count({'user_name':user_name,'password':password}) > 0:
        print('user login successfully')
    else:
        print('user is not registered')
        print('user is being registered')
        ReguisterUser(user_info,user_name,password)


user_info=[dict]
(user_name,password)=input('Enter credentials ').split(',')


LoginUser(user_info,user_name,password)