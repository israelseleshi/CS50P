# for _ in range(3): # pythonic expression if we do not use the variable
#   print("meow")

# print("meow\n" * 3, end = "")

# while True:
#   n = int(input("What's n? "))
#   if n > 0:
#     break

# for _ in range(n):
#   print("meow")

def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      break
  return n

def meow(n):
  for _ in range(n):
    print('meow')

main()