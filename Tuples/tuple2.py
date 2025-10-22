#1 Combine colors and shapes to create a new tuple called art.
#2 Demonstrate how to repeat a tuple, specifically colors three times.
#3 Add an art element called “Diamond” to the art tuple.
#4 Extract and print the middle element from the art tuple using slicing.
#5 Verify if the string "square" exists within the art tuple.

# task 1

colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art=colors+shapes
print(art)

# task 2

colors = ("red", "green", "blue")
x=colors*3
print(x)

# task 3
art=('red', 'green', 'blue', 'circle', 'square', 'triangle')
x=('Diamond',)
art=(art + x)
print(art)

# task 4

art=('red', 'green', 'blue', 'circle', 'square', 'triangle', 'Diamond')
x=(len(art))
y=x//2
z=x-y
print(art[y:z])

# task 5

art=('red', 'green', 'blue', 'circle', 'square', 'triangle', 'Diamond')
if "square" in art:
    print("Yes")
else:
    print("No")


