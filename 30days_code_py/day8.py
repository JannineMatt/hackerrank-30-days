'''
Given N names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number
of names to query your phone book for
for each name queried, print the associated
entry from your phone book(in the form name=phoneNumber) or Not found
if there is no entry for name.
'''

N = int(input())  # how many phone
phone_dict = dict()  # dict of phone book

# enter the phone book
for _ in range(N):
    name, phone_number = input().split()
    phone_dict[name] = phone_number
# query the phone book
for _ in range(N):
    name = input()
    phone_number = phone_dict.get(name, None)
    if phone_number:
        print('{0}={1}'.format(name, phone_number))
    else:
        print('Not found')
