import random

cnt = 0

print("Who are you?")
print(">", end = " ")
Name = str(input())
print("Hello,", Name, end = "")
print("!")

print("Tossing a coin...")
for i in range(3):
    judge = random.randint(0, 100)
    if(judge % 2 == 0):
        S = "Heads"
        cnt += 1
    else:
        S = "Tails"
    print("Round", i, end = "")
    print(":", S)

print("Heads:", cnt, end = "")
print(", Tails:", 3 - cnt)