def permissionToNumber(permission):     # max permission is rwxrwxrwx min permission is ---------
    binary = list("000000000")
    index = 0

    for character in permission:    # Converts permission settings to binary
        if character == '-':
            binary[index] = "0"
        else:
            binary[index] = "1"
        index += 1

    number1 = int("".join(binary[:3]), 2) * 100     # Converts binary to number || Absolutely needs to be improved lol
    mid = "".join(binary[3])
    mid += "".join(binary[4])
    mid += "".join(binary[5])
    number2 = int(mid, 2) * 10
    end = "".join(binary[6])
    end += "".join(binary[7])
    end += "".join(binary[8])
    number3 = int(end, 2)
    print(number1 + number2 + number3)

def numberToPermission(number):     # max number is 777 min number is 000
    binary = ""
    number = list(str(number))
    index = 0

    for numbers in number:     # Converts number to binary
        binary += bin(int(number[index]))
        index += 1

    binary = list(binary)   # Removes the "0b" prefix bin() adds
    del binary[0]
    del binary[0]
    del binary[3]
    del binary[3]
    del binary[6]
    del binary[6]
    binary = "".join(binary)
    permission = ""
    index = 0

    while len(binary) != 9:     # Adds 0's until binary is 9 length
        binary += "0"

    for number in binary:       # Converts binary to permission setting
        if number == '1':
            if index == 0 or index == 3 or index == 6:
                permission += "r"
            elif index == 1 or index == 4 or index == 7:
                permission += "w"
            else:
                permission += "x"
        else:
            permission += "-"
        index += 1

    print(permission)

while True:
    try:
        userInput = int(input("\nWhich would you like to convert? \n1. Permission to number \n2. Number to permission \n-1. Quit program\n"))
        if userInput == 1:
            userPermission = input("\nEnter the permission setting you want (ex. rw-r--r--): ")
            if ("r" in userPermission or "w" in userPermission or "x" in userPermission or "-" in userPermission) and len(userPermission) < 10:    # Verifies user permission input
                permissionToNumber(userPermission)
            else:
                userPermission = int("Intentional Error")

        elif userInput == 2:
            userNumber = int(input("\nEnter the number you would like to see the corresponding permission settings (ex. 775): "))
            numberToPermission(userNumber)

        elif userInput == -1:
            break

        else:
            print("\n-ERROR-\nInvalid choice\n")
    except ValueError:
        print("\n-ERROR-\nInvalid choice\n")

