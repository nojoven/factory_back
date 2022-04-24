import time
import random


def get_result():
    return random.randrange(100) < 60

class Bot:
   """This is the blueprint for our bots"""
   def __init__(self, is_free=True):
    self.is_free = is_free

   def move(self):
      if not self.is_free:
         return
      self.is_free = False
      time.sleep(1)
      self.is_free = True
   
   def mine_foo(self):
      if not self.is_free:
         return
      self.is_free = False
      time.sleep(0.25)
      self.is_free = True

   def mine_bar(self):
      if not self.is_free:
         return
      self.is_free = False
      time.sleep(random.randint(0.1, 0.4))
      self.is_free = True

   def combine(self):
      if not self.is_free:
         return
      self.is_free = False
      time.sleep(0.4)
      self.is_free = True



