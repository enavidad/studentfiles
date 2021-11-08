import logging
import csv
import json

print('Hello')

def file_location():
    print('Please enter a location you would like to save the file such as C:\\Users\\user\\Desktop\\:')
    file_location = input()
    return file_location
def file_name():
    print('Please enter a name for the file:')
    file_name = input()
    return file_name
class User:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
    def getphone(self):
        return self.phone
    def showuser(self):
        print(f'{self.name}\n{self.address}\n{self.phone}\n')

#location = file_location()
#name = file_name()

#Combines file location and name into one
fofficial = file_location() + file_name()

#Makes fofficial a text file
filename = f'{fofficial}.txt'

#User info input
user1 = User(input('Name:'), input("Address:"),input('Phone:'))

#Making a list for JSON
user = [user1.name,user1.address,user1.phone]             

#Writes user info into file using JSON dump
with open(filename, 'a') as f:
    json.dump(user, f)
   
    
#Reading the contents with JSON load   
with open(filename,'r') as f:
    contents = json.load(f)
    print(contents)




