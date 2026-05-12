print("Enter a Character: ")
c = input()
if c>='0' and c<='9':
    print("\nIt is an Number")
elif c>='a' and c<='z':
    print("\nIt is an Alphabet")
elif c>='A' and c<='Z':
    print("\nIt is an Alphabet")
else:
    print("\nIt is a not an Alphabet nor an Number")