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

   def bar_mined(self):
      self.bar += 1

   def combination_result(self, success):
      if success:
         self.foobar += 1
      else:
         self.foo += 1
   
   def init_robot(self):
      self.robots = [] 
      for i in range(self.robots_number):
         self.robots.append(Bot(self.foo_mined, self.bar_mined, self.combination_result))
      return self.robots

   def sell_foobar(self):
      self.foobars -= 5
      print(f"Number of foobars sold: 5. {self.foobar} foobars left")
      
      self.money += 5

   def buy_robot(self):
      before_money = self.money
      before_foos = self.foo
      before_robots = self.robot
      

      if self.money > 3 and self.foo > 6:
         print(f"Before payment: factory owns {before_money} €.")
         print(f"Before payment: factory owns {before_foos} foos.")
         print(f"Before payment: factory owns {before_robots} robots.")

         self.money -= 3
         self.foo -= 6
         self.robots.append(Bot(self.foo_mined, self.bar_mined, self.combination_result))
         print("Factory acquires 1 robot.")
         print(f"Factory spent : {before_money - self.money}€.")
         print(f"After payment : Factory owns {self.money} €.")

         print(f"After payment : consummed {before_foos - self.foo} .")
         print(f"Factory keeps : {self.foo} foos.")

         print(f"Factory had")
         print(f"")





   def work(self):
      print("Production starts.")
      robots = self.init_robot()
   
      while self.robots_number < 30:
         
         for robot in robots:
            if not self.bar:
               print("Not enough bar. Extraction will start.")
               robot.mine_bar(fac.current_time)
               continue
            
            if not self.foo:
               print("Not enough foo. Extraction will start.")
               robot.mine_foo(fac.current_time, 1)
               continue
            
            if self.foo and self.bar:
               "Starting the combination process."
               robot.combine(fac.current_time, 2)
               self.foo -= 1
               self.bar -= 1 
               continue
            
            if self.foobar >= 5:
               before_money = self.money
               print(f"Before sale: factory owns {before_money} €.")
               fac.sell_foobar()
               print(f"After sale: earned {self.money - before_money} €.")
               print(f"Factory owns : {self.money} €.")

         self.current_time += 1

      




if __name__ == "__main__":
   fac = Factory()
   fac.work()