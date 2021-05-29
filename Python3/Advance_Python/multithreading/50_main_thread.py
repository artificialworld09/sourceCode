'''
When we start any Python Program, one thead begins running immediately which is callled Main Thread of that program created by PVM (Python Virtual Machine).
The main tread is created automatically when your program is started.
'''
# print(__doc__)

import threading
t=threading.current_thread().getName() #to get Current Thread
print('The current_thread name is:', t)