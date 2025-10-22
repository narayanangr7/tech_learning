# task 1

fruits =("apple", "banana", "cherry", "mango", "banana")
print(len(fruits))



# task 3

fruits =("apple", "banana", "cherry", "mango", "banana")

y = list(fruits)
y[2] = "grape"
fruits = tuple(y)

print(fruits)