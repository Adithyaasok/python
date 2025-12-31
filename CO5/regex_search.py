
import re
word = input("Enter word: ")
with open("demo.txt","r") as f:
    text = f.read()
matches = re.findall(r"\b"+re.escape(word)+r"\b", text, re.IGNORECASE)
print("Occurrences:", len(matches))
