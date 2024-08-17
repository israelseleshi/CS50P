def main():
    greeting = input("Greeting: ").strip()
    greeting_checker(greeting)

def greeting_checker(g):
    if g.startswith("Hello"):
        print("$0", end = "")
    elif g.startswith("H"):
        print("$20", end = "")
    else:
        print("$100", end = "")

main()
