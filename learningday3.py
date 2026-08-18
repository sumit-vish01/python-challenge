def greet(name):
    print("hello", name)

greet("sumit")


def ai(name):
    print("bkswass", name)

ai("rahul")

def greet(name = "Guest"):

# example

def order_food(food, drink= "water"):
    print("Food",food)
    print("Drink", drink)


# order_food("pizza")

order_food("pizza", "coke")


# requied vs optional parameter

# required parmeter

def add(a, b = 10):
    return a + b

add(5)

def add(a, b):
    return a + b

add(5, 10)