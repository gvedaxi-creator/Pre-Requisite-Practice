while True:
    print("\n========== MENU ==========")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Character to ASCII")
    print("8. ASCII to Character")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter Decimal Number: "))
        print("Binary =", bin(n)[2:])

    elif choice == 2:
        n = int(input("Enter Decimal Number: "))
        print("Octal =", oct(n)[2:])

    elif choice == 3:
        n = int(input("Enter Decimal Number: "))
        print("Hexadecimal =", hex(n)[2:].upper())

    elif choice == 4:
        b = input("Enter Binary Number: ")
        print("Decimal =", int(b, 2))

    elif choice == 5:
        o = input("Enter Octal Number: ")
        print("Decimal =", int(o, 8))

    elif choice == 6:
        h = input("Enter Hexadecimal Number: ")
        print("Decimal =", int(h, 16))

    elif choice == 7:
        ch = input("Enter a Character: ")
        print("ASCII Value =", ord(ch))

    elif choice == 8:
        num = int(input("Enter ASCII Value: "))
        print("Character =", chr(num))

    elif choice == 9:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")