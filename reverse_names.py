names = input("Enter names: ").split()
print("Reversed:", names[::-1])
print("Longest:", max(names, key=len))
