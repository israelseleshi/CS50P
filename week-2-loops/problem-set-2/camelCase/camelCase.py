def main():
  text = input("camelCase: ").strip()
  result = snake_case(text)
  print("snake_case:", result)

def snake_case(text):
  result = ""
  for t in text:
    if t.isupper():
      t = t.lower()
      result = result + f"_{t}"
    else:
      result = result + t
  return result

if __name__ == "__main__":
  main()