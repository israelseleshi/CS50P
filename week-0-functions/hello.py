# # Ask user for their name
# name = input("What's your name? ")

# # Say hello to user
# print(f"hello, {name}")


def main():
  name = input("What's your name? ")
  hello(name)

def hello(to = "world"):
  print("hello,", to)

main()