import sched
import time

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()


# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')

import time
from threading import Thread

def schedule_function2(event_time, function, *args):
    delay = event_time - time.time()  # Calculate how much time to wait
    if delay > 0:
        time.sleep(delay)  # Sleep for the required delay
    function(*args)  # Call the function with the provided arguments

def threaded_schedule_function(event_time, function, *args):
    # Run the schedule_function in a separate thread
    thread = Thread(target=schedule_function2, args=(event_time, function, *args))
    thread.start()
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')


# Commands used in solution video for reference
if __name__ == '__main__':
    event_time1 = time.time() + 1  # 1 second later
    event_time2 = time.time() + 2  # 1 second later

    threaded_schedule_function(event_time1, print, 'Howdy!')
    threaded_schedule_function(event_time2, print, 'Howdy!', 'How are you?')