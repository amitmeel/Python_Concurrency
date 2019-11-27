from threading import Thread, Lock
import time

###using Lock to run a single thread at a time
# thread synchronization


class MyThread(Thread):
    def __init__(self, name, delay):
        # super(MyThread,self).__init__()  
        Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Strating Thread {self.name}')
        thread_lock.acquire()
        thread_count_down(self.name, self.delay)
        thread_lock.release()
        print(f'Finished thread {self.name}')

def thread_count_down(name, delay):

    counter = 5

    while counter:
        time.sleep(delay)
        print(f'Thread {name} counting down {counter}')
        counter -= 1

thread_lock = Lock()
thread1 = MyThread('A',0.5)
thread2 = MyThread('B',0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Finished')