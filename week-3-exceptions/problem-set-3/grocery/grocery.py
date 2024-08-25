def main():
  grocery = {}
  while True:
    try:
      item = input("Add: ").strip().upper()
    except EOFError:
      break
    except KeyError:
      pass
    
    if item in grocery:
      grocery[item] += 1
    else:
      grocery[item] = 1

  for item in sorted(grocery.keys()):
    print(f'{grocery[item]} {item}')


if __name__ == "__main__":
  main()
