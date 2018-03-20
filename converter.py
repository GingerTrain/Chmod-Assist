def permission_to_number(permission):     # Max permission is rwxrwxrwx min permission is ---------
    binary = list("000000000")
    index = 0

    for character in permission:    # Converts permission settings to binary
        if character == '-':
            binary[index] = "0"
        else:
            binary[index] = "1"
        index += 1

    number1 = int("".join(binary[:3]), 2) * 100     # Converts binary to number ** Needs improvement
    mid = "".join(binary[3])
    mid += "".join(binary[4])
    mid += "".join(binary[5])
    number2 = int(mid, 2) * 10
    end = "".join(binary[6])
    end += "".join(binary[7])
    end += "".join(binary[8])
    number3 = int(end, 2)
    return "The corresponding number is: " + str(number1 + number2 + number3)


def number_to_permission(number):       # Max number is 777 min number is 000
    if number == 0 or number == 00 or number == 000:
        return "The corresponding permission is: ---------"

    binary = list()
    number = list(str(number))
    index = 0

    for numbers in number:     # Converts number to binary
        if int(numbers) == 0:
            binary += bin(int(number[index]))
            binary.append("0")
            binary.append("0")
        elif int(numbers) == 1:
            binary += bin(int(number[index]))
            binary.insert(-1, "0")
            binary.insert(-1, "0")
        elif int(numbers) <= 3:
            binary += bin(int(number[index]))
            binary.insert(-2, "0")
        elif int(numbers) > 7:
            return int("Intentional Error")
        else:
            binary += bin(int(number[index]))
        index += 1

    binary = list(binary)   # Removes the "0b" prefix bin() adds ** Needs improvement
    print(binary)
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

    return "The corresponding permission is: " + permission


def verify_permission(permission):        # Max permission is rwxrwxrwx min permission is ---------
    r = [permission[0], permission[3], permission[6]]
    w = [permission[1], permission[4], permission[7]]
    x = [permission[2], permission[5], permission[8]]
    condition = 0

    for index in r:
        if index == "r" or index == "-":
            continue
        else:
            return int("Intentional Error")
    condition += 1
    for index in w:
        if index == "w" or index == "-":
            continue
        else:
            return int("Intentional Error")
    condition += 1
    for index in x:
        if index == "x" or index == "-":
            continue
        else:
            return int("Intentional Error")
    condition += 1

    if condition == 3:
        return "valid"


while True:
    try:
        userInput = int(input("\nChoose an option: \n1. Permission to number \n2. Number to permission "
                              "\n-1. Quit program\n"))
        if userInput == 1:
            userPermission = input("\nEnter the permission setting you want (ex. rw-r--r--): ")
            if len(userPermission) != 9:
                int("Intentional Error")
            elif verify_permission(userPermission) == "valid":
                print(permission_to_number(userPermission))
            else:
                int("Intentional Error")

        elif userInput == 2:
            userNumber = str(input("\nEnter the number you want (ex. 775): "))
            if len(userNumber) == 3:
                print(number_to_permission(int(userNumber)))
            else:
                int("Intentional Error")

        elif userInput == -1:
            break

        else:
            print("\n-ERROR-\nInvalid choice\n")
    except ValueError:
        print("\n-ERROR-\nInvalid choice\n")

