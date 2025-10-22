# Perform the following operations:
# Determine the highest and lowest marks.
# Count the occurrences of the mark 85.
# Calculate the average marks using the sum() and len() functions.

# task 1
marks = (78, 85, 69, 90, 85)
highest = max(marks)
lowest = min(marks)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
 

# task 3
marks = (78, 85, 69, 90, 85)
count_85 = marks.count(85)
print("Number of times 85 appears:", count_85)


# task 3
marks = (78, 85, 69, 90, 85)
average = sum(marks) / len(marks)
print("Average marks:", average)
