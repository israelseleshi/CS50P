def main():
    mass = int(input("m: "))
    energy = emc(mass)
    print(f"E: {energy}")

def emc(m):
    return m * 90000000000000000

main()
