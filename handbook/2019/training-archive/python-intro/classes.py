#!/usr/bin/env python

class Person:
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def greet(self):
    print("Hello " + self.name)

  def report_id(self):
    print("Id =" + str(self.id))

p1 = Person("John", 36)
p2 = Person("Paul", 32)
p3 = Person("Kim", 33)
p1.greet()
p3.greet()
p2.report_id()
p3.report_id()
