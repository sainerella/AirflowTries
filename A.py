import functools
import time


class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


dog1 = Dog("Bo", 8)
dog2 = Dog("Snowy", 5)

print(dog1.name)
print(type(dog1))
print(dog1.speak("Woof"))


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for __ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(1)
waste_some_time(99)
