# task 1

fruits =("apple", "banana", "cherry", "mango", "banana")
print(len(fruits))

# task 2
fruits =("apple", "banana", "cherry", "mango", "banana")
x=(fruits.index("banana"))
print(x)

# task 3

fruits =("apple", "banana", "cherry", "mango", "banana")

y = list(fruits)
y[2] = "grape"
fruits = tuple(y)

print(fruits)

# task 4

fruits = ("apple", "banana", "cherry", "mango", "banana")
fruits=[fruits]
print(type(fruits))
fruits=(tuple(fruits))
print(type(fruits))