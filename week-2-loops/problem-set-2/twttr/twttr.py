def main():
  user_input = input("Input: ")
  output = omit_vowel(user_input)
  print(f"Output: {output}")

def omit_vowel(text):
  output = ""
  for t in text:
    if t in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', ]:
      continue
    else:
      output = output + t
  return output


if __name__ == "__main__":
  main()