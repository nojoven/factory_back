from robots import Bot


class Factory:
   def __init__(self, robots_number=2, foo=0, bar=0, foobar=0, money=0):
      self.robots_number = robots_number
      self.bar = bar
      self.foo = foo
      self.foobar = foobar
      self.money = money
      self.init_robot()
   
   def init_robot(self):
      self.robots = [] 
      for i in range(self.robots_number):
         self.robots.append(Bot())

   def work(self):
      while self.robots_number < 30:
         break







if __name__ == "__main__":
   work()