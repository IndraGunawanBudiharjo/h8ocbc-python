def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

object_generator = counter_generator(5, 10)