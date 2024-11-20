import threading
import time

def runner(name, count):
    """ Thread running function. """

    for i in range(count):
        print(f"Running: {name} {i}")
        time.sleep(0.2)  # seconds

def range_sum(name, count, range_):
    print(f'{name} Working on range {count}: {range_}') 
    total_sum = 0
    for i in range(range_[0], range_[1]+1):
        total_sum += i
    results[count] = total_sum
    print(total_sum)
ranges = []
ranges_sum = 0
ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

# Launch this many threads
THREAD_COUNT = len(ranges)

# print(THREAD_COUNT)
results = [0] * THREAD_COUNT


# We need to keep track of them so that we can join() them later. We'll
# put all the thread references into this array
threads = []

# Launch all threads!!
for i in range(THREAD_COUNT):

    # Give them a name
    name = f"Thread{i}"

    # Set up the thread object. We're going to run the function called
    # "runner" and pass it two arguments: the thread's name and count:
    t = threading.Thread(target=range_sum, args=(name, i, ranges[i]))

    # The thread won't start executing until we call `start()`:
    t.start()
        
    threads.append(t)


    # Keep track of this thread so we can join() it later.
    

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.
print(results)

for t in threads:
    t.join()
for i in results:

  ranges_sum += i
print(f'Sum of ranges: {ranges_sum}')