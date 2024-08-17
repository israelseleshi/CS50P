def main():
    expression = input("Expression: ")
    operate(expression)

def operate(e):
    x, y, z = e.split(" ")
    x, z = float(x), float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/" and  z != 0:
        print(x / z)

main()
