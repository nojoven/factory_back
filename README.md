# factory_back

The goal is to code an automatic production line of foobar. 
1- The Factory instantiates 2 robots at the begining.
2- The Factory sends instructions and callback methods to all the robots every second.
3- Each robot calculates the time needed to perform a task based on the current time.
4- If the robot is busy, it does not obey. 
5- Otherwise, it obeys. If the new task is different from the previous one, it will take 5 more seconds to move to a new workstation.
6- When a task is completed the robot uses the callback function of is task to inform the factory of the completion. 
7- When enough foobars are assembled, the factory sells foobars to earn money.
8- When the factory has enough foos and money, it buys a new robot.
9- The factory stops its production when it acquires the 30th robot.
