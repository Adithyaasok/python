colors = input("Enter colors separated by comma: ").split(",")
colors = [c.strip() for c in colors]
print("First Color:", colors[0])
print("Last Color:", colors[-1])
