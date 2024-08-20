amount_due = 50
print(f"Amount Due: {amount_due}")

while True:
  coin = int(input("Insert coin: "))
  if coin not in [25, 10, 5]:
    print("Acceptable coins are only [25, 10, 5]")
    print(f"Amount Due: {amount_due}")
  elif amount_due - coin> 0:
    amount_due -= coin
    print(f"Amount Due: {amount_due}")
  else :
    amount_due -= coin
    print(f"Change Owed: {abs(amount_due)}")
    break
