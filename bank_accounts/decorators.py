from datetime import datetime

def time():
    current_time = datetime.now()
    return current_time
def decorator(myFunction):
    def wrapper():
        print("***************")
        print(myFunction())
        print("***************")
    return wrapper()

current_time = decorator(time)










