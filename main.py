# # number 1
# MyList = [23, 45, 66, 75, 54]
# MyList.reverse()
# print(MyList)
#
# # number 2
# MyList = [23, 45, 66, 75, 54]
# def power(MyList):
#     return [n**2 for n in MyList]
# print(power(MyList))
#
# # number 3
#
# List1 = [1, 3, 5, 6, 7]
# List2 = [6, 7, 8, 40, 6, 66]
# List2.reverse()
# print(f'{List1}{List2}')
#
# # number 5
# Mytuple = (1, 3, 4, 5, 6, 7, 8)
# a = (1, 3)
# b = (4, 5)
# c = (6, 7)
# d = (8,)
# print(a)
# print(b)
# print(c)
# print(d)
#
#
#
# # number 4
# item = [10, 20, [300, 400, [500, 600], 500], 30, 40]
#
# item[2][2].insert(2, 700)
# print(item)
#
# # number6
# import cmath
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = cmath.sqrt(b**2 - 4*a*c)
#
# quadratriceqxn1 = -b + d / (2*a)
# quadraticeqxn2 = -b - d / (2*a)
# print(f'{quadratriceqxn1}\n or\n {quadraticeqxn2}')
#
# # number 7
#
# name = input()
# surname = input()
# age = input()
# address = input()
#
# print(f'''Hello {name}{surname}
# you are {age} years old
# you are living in {address}''')
#
# # number 8
#
# MyTuple = (11, [22, 33], 44, 55 )
# modification = list(MyTuple)
# modification[1][0] = 222
# MyTuple = tuple(modification)
# print(MyTuple)
#
# # number 9
#
# print(int(2.5))
#
# # number 10
# print(upper('Gomindz'))

# my_set = {'sarah', 'Mike', 'jon','jon', "Mike"}
#
# my_dict = {
#     "class" : "jaina",
#     "teacher" : "saye",
#     "baller" : "keita"
# }
#
# my_dict["name"] = "rhyme machine"
# print(my_dict)
#
# gomindz =  my_dict.copy()
#
# print(gomindz)

#
# x = {
#     'a' : 'abie',
#     'b' : "abubacar",
#     'c' : 'ceesay'}
#
# for z in x:
#     print(z)

# print('Python'=='PYTHON')
# print('PYTHON'=='PYTHON')
# print('PYTHON'!='PYTHON')
# print(15!=10)
#
#
# print('hello'!='HELLO'and(6>2)and(5==5))
# print('Hello'!='HELLO'or(6>2)or(5==5))
#
# x=20
# y=30
#
#
# print(x==y)
# print(x!=y)
# print(x<y)
# print(x>y)
# print(x==y or x!=y)
# print(x==y and x!=y)

# NUMBER 5
# import random
# Number = int(input('please enter a number:'))
# RGN = random.randint(1,100)
# print(RGN)
#
# if Number > RGN:
#     print('your number is higher')
# else:
#     print('your number is lower')
# NUMBER 6




# number 7

# script = int(input('please enter an integer: '))
# if script % 5 == 0 and script % 7 != 0:
#     print('the number is valid')
# else:
#     print('the number is not valid')



#coding with mosh

# rating = 4.9
# naame = "musa"
# is_published = True
#
#
# name = "John Smith"
# age = 20
# is_new = True

# name = input('what is your name? ')
# print('Hi ' + name)

# name = input('what is your name ')
# favourite_color = input('what is your favourite colour? ')
# print(name + ' likes ' + favourite_colour)

# weight_pounds = float(input('weight in pounds: '))
# weight_kg = weight_pounds / 2.20462
# print(weight_kg)

# name = 'Jennifer'
# print(name[1:-1])
# len()
# .upper
# .find
# .replace for replacing
# '...' in y true or false

 # round() rounds up
 # abs() for absulute value

 # learn pytho 3 math module

# house_price = 1000000
# has_good_credit = True
# if has_good_credit:
#     downpayment = 0.1 * house_price
# else:
#     downpayment = 0.2 * house_price
# print(f'your discounted price is: {downpayment}')
#
#
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


music_player = tkr.Tk()
music_player.title('Music Player')
music_player.geometry("500x400")

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

playlist = tkr.Listbox(music_player, font = 'verdone 12 bold', fg = "navy", bg = 'gold', selectmode=tkr.SINGLE)


x = 0
for i in song_list:
    playlist.insert(x, i)
    x += 1
    pygame.init()
    pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(music_player, width=5, height=3, font= 'verdone 12 bold', text="PLAY", command=play, bg='navy', fg= 'gold')
Button2 = tkr.Button(music_player, width=5, height=3, font='verdone 12 bold', text="STOP", command=stop, bg='navy', fg= 'gold' )
Button3 = tkr.Button(music_player, width=5, height=3, font= 'verdone 12 bold', text="PAUSE", command=pause, bg='navy', fg= 'gold')
Button4 = tkr.Button(music_player, width=5, height=3, font= 'verdone 12 bold', text="UNPAUSE", command=unpause, bg='navy', fg= 'gold')

var = tkr.StringVar()
song_title = tkr.Label(music_player, font='verdone 12 bold', textvariable=var)

song_title.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
playlist.pack(fill='both', expand= 2)

music_player.mainloop()

password = 2001
max_password_attempts = 5

while  max_password_attempts != 0:
    ask_password = int(input('please enter your pasword: '))
    max_password_attempts -= 1
    if ask_password != password:
        print(f'try again you have {max_password_attempts} tries')
    else:
        print('you have successfully logged in')
        break
def myfunction():
    print("the function is this")
myfunction()

def myfunction(firstvalue,secondvalue):
    result = firstvalue + secondvalue
    print(result)
myfunction(5,4)

def function(value1, value2):
    result = value1 - value2
    print(result)

function(9,3)

