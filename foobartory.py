import time
import random
from robots.robots import Bot


class Factory:
   
   def __init__(self, robots_number=2, foo=0, bar=0, foobar=0, money=0):
      self.robots_number = robots_number
      self.bar = bar
      self.foo = foo
      self.foobar = foobar
      self.money = money
      self.current_time = 0
      self.init_robot()

   def foo_mined(self):
      self.foo += 1
      print(f"Mined 1 foo. Total foo = {self.foo}")

   def bar_mined(self):
      self.bar += 1
      print(f"Mined 1 bar. Total bar = {self.bar}")

   def combination_result(self, success):
      print(f"Combine 1 FOOBAR. Total foobar = {self.foobar}")
      if success:
         self.foobar += 1
         print(f"SUCCESSFUL COMBINATION. Total foobar = {self.foobar}")
      else:
         self.foo += 1
         print(f"FAILURE WHILE COMBINING. Total foobar = {self.foobar}. ")
         print(f"1 FOO LOST. Total foo = {self.foo}")
   
   def init_robot(self):
      self.robots = [] 
      for i in range(self.robots_number):
         self.robots.append(Bot(self.foo_mined, self.bar_mined, self.combination_result))
      return self.robots

   def sell_foobar(self):
      self.foobar -= 5
      print(f"Number of foobars sold: 5. {self.foobar} foobars left")
      self.money += 5

   def buy_robot(self):
      before_money = self.money
      before_foos = self.foo
      before_robots = self.robots_number
      print(f"BEFORE PURCHASE.")
      print(f"Factory owns {before_foos} foos.")
      print(f"Factory owns {before_money} €.")
      print(f"Factory owns {before_robots} robots.")
      
      print("BUYING NEW ROBOT!")
      self.money -= 3
      self.robots.append(Bot(self.foo_mined, self.bar_mined, self.combination_result))
      self.foo -= 6
      self.robots_number += 1

      print(f"AFTER THE PURCHASE.")
      print(f"Factory has {self.robots_number} robots left.")
      print(f"Factory has {self.foo} foos left.")
      print(f"Factory has {self.money} € left.")

      

         





   def work(self):
      print("Production starts.")
      robots = self.init_robot()
   
      while self.robots_number < 30:
         
         if self.money >= 3 and self.foo > 6 :
            print("Factory orders a NEW robot! ")
            self.buy_robot()

         for robot in robots:

            if self.foobar >= 5:
               before_money = self.money
               print(f"Before sale: factory owns {before_money} €.")
               self.sell_foobar()
               print(f"After sale: earned {self.money - before_money} €.")
               print(f"Factory owns : {self.money} €.")
               continue

            if self.bar < 3:
               print("Not enough bar. Extraction will start.")
               robot.mine_bar(fac.current_time)
               continue
            
            if self.foo < 7:
               print("Not enough foo. Extraction will start.")
               robot.mine_foo(fac.current_time, 1)
               continue
            
            if self.foo and self.bar and self.foo > 6:
               "Starting the combination process."
               robot.combine(fac.current_time, 2)
               self.foo -= 1
               self.bar -= 1 
               continue
            
         self.current_time += 1


if __name__ == "__main__":
   fac = Factory()
   fac.work()