#nested loops
rows = int(input("How many Rows? :"))
columns = int(input('How many rows?: '))
symbol = input("Enter a symbol to use : ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end =" ")
    print()

