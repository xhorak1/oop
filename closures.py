

def counter():
    number = 0

    def increment():
        nonlocal number
        number += 1
        return number

    return increment

c = counter()
print(c())
print(c())



def print_Hello():
    print("Hello")

pozdrav = print_Hello()
pozdrav2 = print_Hello

print(pozdrav)
print(pozdrav2)

pozdrav2()
print_Hello()