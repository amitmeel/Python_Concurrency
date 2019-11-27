from threading import Thread, Lock
import time
import queue

###using Lock to run a single thread at a time
# thread synchronization


class MyThread(Thread):
    def __init__(self, name, delay):
        # super(MyThread,self).__init__()  
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f'Strating Thread {self.name}')
        thread_call(self.name)
        print(f'Finished thread {self.name}')

def thread_call(name):
    print(f'Thread {name} starting sum')
    x = q.get(block=False)
    y = q.get(block=False)
    sum(x,y)

def sum(x,y):
    print('sum', (x+y))

q = queue.Queue()

_input = [1,2,3,4]
for x in _input:
    q.put(x)

thread1 = MyThread('A',0.5)
thread2 = MyThread('B',0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Finished')