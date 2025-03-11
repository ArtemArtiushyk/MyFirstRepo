try:
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")

except ValueError:
    print("Number mustn't have any letters")
