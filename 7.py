# 01-bits-and-binary.py
# Topic: Bits and Binary Numbers, AND and OR

n = int(input("Enter a number (try 5 or 12): "))
guess = input("Guess its binary: ")

input("Binary. Press Enter ")
print("  decimal", n, "-> binary", bin(n)[2:])
print("  Your guess:", guess)

input("AND - both bits must be 1.")