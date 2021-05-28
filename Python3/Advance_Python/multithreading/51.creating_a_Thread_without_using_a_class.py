'''
Thread class of threading module is used to create threads. To create our own thread we need to create an object of Thread Class.

Following are the ways of creating threads:-
1.Creating a thread without using a class.
2.Creating a thread by creating a child class to Thread class.
3.Creating a thread without creating child class to Thread class.



CREATING A THREAD WITHOUT USING A CLASS
thread_object = Thread(target=function_name, args=(arg1, arg2, ....))

Exp:
from threading import Thread
t=Thread(target=disp, args=(10, 20))

thread_object: It represents our thread.
target: It represents the function on which the thread will act.
args: It represents a tuple of arguments which are passed to the function.



STARTING A THREAD
Once a thread is created it should be started by calling start() method.

Exp:
from threading import Thread
def disp(a, b):
    print('Thread Running:', a,b)
t=Thread(target=disp, args=(10, 20))
t.start() #starting a Thread

Exp2:
from threading import Thread
def disp(a, b):
    print('Thread Running', a,b)
for i in range(5):
    t=Thread(target=disp, args=(10, 20))
    t.start() #starting a Thread

17:20/22:01
'''

# from threading import Thread
# def disp():
#     print('Thread Running...')
# t=Thread(target=disp)
# t.start() #starting a Thread


# from threading import Thread
# def disp(a, b):
#     print('Thread Running:', a,b)
# t=Thread(target=disp, args=(10, 20))
# t.start() #starting a Thread


# from threading import Thread
# def disp(a, b):
#     print('Thread Running', a,b)
# for i in range(5):
#     t=Thread(target=disp, args=(10, 20))
#     t.start() #starting a Thread


from threading import Thread
def disp():
    for i in range(5):
        print('\tChild Thread')
t=Thread(target=disp)
t.start()

for i in range(5):
    print('Main Thread...')