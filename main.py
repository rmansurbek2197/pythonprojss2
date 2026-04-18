import logging
import functools

logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(a, b):
    return a * b

@log_decorator
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

print(add(2, 3))
print(multiply(4, 5))
print(divide(10, 2))