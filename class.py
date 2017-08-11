from bs4 import BeautifulSoup
import os
import requests
class people:
   name = ""
   age = 0
   __weight = 0
   def __init__(self, n, a, w):
       self.name = n
       self.age = a
       self.__weight = w
   def speak(self):
       print('{}说:我{}岁'.format(self.name, self.age))
   
p = people('pan', 18, 65)
p.speak()

class stu(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("{name}说：我{age} 岁, 我上{grad} 年级".format(name = self.name, age = self.age, grad = self.grade))

s = stu('xu', 18, 34, 3)
s.speak()

oup = BeautifulSoup()

