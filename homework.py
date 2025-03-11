try:
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")

except ValueError:
    print("Number mustn't contain any letters")

print(f"This is a table of {3} multiplied by numbers from 1 to 10.")
