import time
import random




class Bot:
   """This is the blueprint for our bots"""
   def __init__(self, busy_until=0):
      self.busy_until = busy_until

   def move(self, current_time, execution_time=1):
      if not self.is_free:
         return
      self.busy_until = False
   
   def mine_foo(self, current_time, foo_mined, execution_time=0.25):
      if not self.is_free:
         return
      self.busy_until = False

   def mine_bar(self,current_time, bar_mined, execution_time=random.randint(0.1, 0.4)):
      if not self.is_free:
         return
      self.busy_until = False

   def combine(self, current_time, combination_result, execution_time=0.4):
      if not self.is_busy:
         is_successful = random.randrange(100) < 60

      self.busy_until = False



