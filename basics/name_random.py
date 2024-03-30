import random

names = ["Rohan", "Kashish", "Naveen", "Renu"]
nlen = len(names)
num = random.randint(0, nlen -1)
print(f"{names[num]} will have to pay the bill")
