text = input("Enter text: ")
words = text.split()
count = {}
for w in words:
    count[w] = count.get(w,0)+1
print(count)
