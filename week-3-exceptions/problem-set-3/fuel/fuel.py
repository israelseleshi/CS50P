def main():
  while True:
    try:
      fuel = input("Fraction: ")
      if '/' not in fuel:
        print("Invalid input format. Use the format X/Y.")
        continue

      num1, num2 = fuel.split('/')
      num1, num2 = int(num1), int(num2)

      if num1 > num2:
        print("Numerator cannot be greater than denomiator.")
        continue

      percentage = round((num1 / num2) * 100)

      if percentage <= 1:
        print("E")
        break
      elif percentage >= 99:
        print("F")
        break
      else:
        print(f"{percentage}%")
        break

    except ValueError:
      print("Invalid input. Please enter a valid fraction in the format X/Y.")
    except ZeroDivisionError:
      print("Invalid input: Division by zero.")



if __name__ == "__main__":
  main()
