# Define a decorator factory repeat(n) which takes int n and return decorator 
# Decorator should allow that the function is called n times until n is exhausted

def repeat(n):
    count = 0
    def inner(func):
        def wrapper(*args):
            print("Running the func..")
            for i in range(n):
                nonlocal count
                count+=1
                try:
                    result = func(*args)

                    print(f"Done: {count} time")
                except Exception as e:
                    print(e)
            return result
        return wrapper
    return inner




@repeat(3)
def say_hello(name):
    print(f"Hello {name}")

z = say_hello('Luka')