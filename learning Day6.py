import math
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.keys():
    print(product)

for price in products.values():
    print(price)

for product in products:
    print(product)

for product in products.items():
    print(product)

for product, price in products.items():
    print(product, price)

for price, product in products.items():
    print(price, product)

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

for product in enumerate(products):
    print(product)

for index, product in enumerate(products):
    print(index, product)

for price in enumerate(products.values()):
    print(price)

for index, price in enumerate(products.values()):
    print(index, price)

for index, product in enumerate(products.items()):
    print(index, product)

for index, product in enumerate(products.items(),1):
    print(index, product)



my_sets = {2, 4,5 }
set()
{}

my_set = {1, 2, 3,4 , 6 }
my_set.add(9)
my_set.remove(4)
my_set.discard(2)
my_set.clear()
print(my_set)

my_set = {1, 2, 3,4 , 6 }
your_set =  { 2, 3,4 , 6 }

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))
print(my_set.isdisjoint(your_set))


my_set = {1, 2, 3,4 , 5}
your_set = { 2, 3,4 , 6}

print(your_set.issubset(my_set))
print(my_set.issuperset(your_set))
print(my_set.isdisjoint(your_set))

my_set | your_set
my_set & your_set
my_set ^ your_set
my_set - your_set
# my_set -= your_set
print(my_set)

print(5 in my_set)
