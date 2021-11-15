# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'

# print(my_generator())
# print(list(my_generator()))

# print('print with for')
# for char in my_generator():
#     print(char)

# def counter_generator(low, high):
#     while low <= high:
#         yield low
#         low += 1

# object_generator = counter_generator(5, 10)
# print(next(object_generator))

# for i in counter_generator(5,10):
#     print(i, end=' ')

'''
1, h --> yield low
5 10 --> 5 
6 10 --> 6
7 10 --> 7
8 10 --> 8
9 10 --> 9
10 10 --> 10
'''

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# for i in infinite_sequence():
#     print(i, end=" ")

'''
num     yield num
0   --> 0
1   --> 1
2   --> 2
... 
'''

# first class function

# def say_hello(name):
#     return f'Hello {name}'

# def be_awesome(name):
#     return f'Yo {name}, together we are the awesomest!'

# def weather_talk(name):
#     return f'The weather is nice, {name}.'

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))
# print(greet_bob(weather_talk))

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])