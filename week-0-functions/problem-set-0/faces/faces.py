def main():
    # Asking to user to enter text
    text = input("Enter text to test: ")
    result = convert(text)
    print(result)

def convert(t):
    # converts :) to 🙂
    t = t.replace(":)", "🙂")
    # converts:( to 🙁
    t = t.replace(":(", "🙁")
    # returns final result
    return t

main()
