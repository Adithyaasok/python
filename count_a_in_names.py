names = input("Enter names separated by comma: ").split(",")
count = 0
for name in names:
    count += name.lower().count('a')
print("Number of elements:", len(names))
print("Count of 'a':", count)
