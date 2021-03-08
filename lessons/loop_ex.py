"""Examples using loops"""

count: int = 0
while input("Do you need more love? yes/no -") == "yes":
    #Body block of the while loop is evaluated
    #When the expresion is true
    print("I love you!")
    count += 1
    print(f"Count is {count}")

print("Have a lovely day!")
