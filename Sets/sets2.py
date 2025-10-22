rainfall_data = { 120, 150, 180, 120, 90, 110, 130}
# (This set represents the rainfall in mm recorded across various districts this week.)
# How many rainfall values are in the set?
print(len(rainfall_data))
# Can you directly change the value of an item in a set?
#  What output would you get when you try to change the value using its index ?
# rainfall_data[2] = 100
# print(rainfall_data)
# Check if 150 is present inside rainfall_data. (hint: use in keyword and research)
if 150 in rainfall_data:
    print("Yes")
else:
    print("No")
# Convert the set to a list
new = list(rainfall_data)
print(new)
# Print every rainfall value by traversing through the set.
for i in rainfall_data:
    print(i)
# Remove the value 120 from the above set.
rainfall_data.remove(120)
print(rainfall_data)
# Add the value 110 to the above set and observe if any changes happen ?
# Why does 110 not appear twice ?
rainfall_data.add(110)
print(rainfall_data)
