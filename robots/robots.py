import time
import random


class Task:
   def __init__(self, completion_time, callback_method, task_result=None):
      self.completion_time = completion_time
      self.task_result = task_result
      self.callback_method = callback_method

   def perform(self):
      if self.task_result is not None:
         print(f"I have finished {self.callback_method}.")
         self.callback_method(self.task_result)
      else:
         print(f"I am going to start {self.callback_method}.")
         self.callback_method()
         print(f"I am performing {self.callback_method}.")




class Bot:
   """This is the blueprint for our bots"""

   def __init__(
         self, 
         foo_mined, 
         bar_mined,
         combination_result,
         busy_until=0):
      self.busy_until = busy_until
      self.foo_mined = foo_mined
      self.bar_mined = bar_mined
      self.combination_result = combination_result
      self.task = None

   def is_same_task(self, callback_method):
         return self.task is not None and self.task.callback_method == callback_method

   def mine_foo(self, current_time, execution_time=1):
      print("Received order : Mine foo !")
      if self.busy_until > current_time:
         print("Foo? I am busy.")
         return
      self.perform_task(current_time)

      self.busy_until = current_time + execution_time
      completion_time = self.busy_until if self.is_same_task(self.foo_mined) else self.busy_until + 5
      self.task = Task(completion_time, self.foo_mined)

   def mine_bar(self,current_time, execution_time=(random.uniform(0.5, 2))):
      if self.busy_until > current_time:
         print("Bar? I am busy.")
         return
      self.perform_task(current_time)

      self.busy_until = current_time + execution_time
      print(f"I will be busy until {self.busy_until}.")

      completion_time = self.busy_until if self.is_same_task(self.bar_mined) else self.busy_until + 5
      print(f"Required completion time = {completion_time}.")
      
      self.task = Task(completion_time, self.bar_mined)

   def combine(self, current_time, execution_time=2):
      
      if self.busy_until > current_time:
         print("I am busy.")
         return
      self.perform_task(current_time)

      self.busy_until = current_time + execution_time
      print(f"I will be busy until {self.busy_until}.")
      
      completion_time = self.busy_until if self.is_same_task(self.combination_result) else self.busy_until + 5
      print(f"Required completion time = {completion_time}.")

      self.task = Task(completion_time, self.combination_result, random.randrange(100) < 60)

   def perform_task(self, current_time):
      if self.task and self.task.completion_time > current_time :
         self.task.perform()
         self.task = None
