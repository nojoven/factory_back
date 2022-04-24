from robots import Bot


class Factory:
   current_time = 0
   def __init__(self, robots_number=2, foo=0, bar=0, foobar=0, money=0):
      self.robots_number = robots_number
      self.bar = bar
      self.foo = foo
      self.foobar = foobar
      self.money = money
      self.init_robot()

   def foo_mined(self):
      self.foo += 1

   def bar_mined(self):
      self.bar += 1

   def combination_result(self, success):
      if success:
         self.foobar += 1
         self.bar -= 1
         self.foo -= 1
      else:
         self.bar -= 1
   
   def init_robot(self):
      self.robots = [] 
      for i in range(self.robots_number):
         self.robots.append(Bot())

   def work(self):
      while self.robots_number < 30:
         current_time += 1
         break







if __name__ == "__main__":
   work()