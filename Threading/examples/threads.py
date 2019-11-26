from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Strating Thread {self.name}')
        thread_count_down(self.name, self.delay)
        print(f'Finished thread {self.name}')

def thread_count_down(name, delay):

    counter = 5

    while counter:
        time.sleep(delay)
        print(f'Thread {name} counting down {counter}')
        counter -= 1

thread1 = MyThread('A',0.5)
thread2 = MyThread('B',0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Finished')