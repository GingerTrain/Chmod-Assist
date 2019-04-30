'''
NOTE:
    Max symbolic permission is rwxrwxrwx, min symbolic permission is ---------
    Max numeric permission is 777, min numeric permission is 000
'''

from enum import Enum
import operator


class Menu(Enum):
    SYM2NUM = 1
    NUM2SYM = 2
    EXIT = 3
    RANGE = range(1, 4)
    ERROR = "\n-ERROR-\nPlease only use the values specified, thank you"


# Converts from symbolic permission to numeric permission
def symbolic_to_numeric(sym_permission):
    binary = list("000000000")
    index = 0

    # Converts symbolic permission to binary
    for character in sym_permission:
        if character == '-':
            binary[index] = "0"
        else:
            binary[index] = "1"
        index += 1

    # Converts binary to numeric permission TODO: Refactor
    first_digit = int("".join(binary[:3]), 2) * 100
    mid = "".join(binary[3])
    mid += "".join(binary[4])
    mid += "".join(binary[5])
    second_digit = int(mid, 2) * 10
    end = "".join(binary[6])
    end += "".join(binary[7])
    end += "".join(binary[8])
    third_digit = int(end, 2)

    return str(first_digit + second_digit + third_digit)


# Converts from numeric permission to symbolic permission
def numeric_to_symbolic(num_permission):
    if num_permission == "000":
        return "---------"

    binary = list()
    num_permission = list(num_permission)
    index = 0

    # Converts numeric permission to binary
    for number in num_permission:
        if number == "0":
            binary += bin(int(num_permission[index]))
            binary.append("0")
            binary.append("0")
        elif number == "1":
            binary += bin(int(num_permission[index]))
            binary.insert(-1, "0")
            binary.insert(-1, "0")
        elif number <= "3":
            binary += bin(int(num_permission[index]))
            binary.insert(-2, "0")
        elif number > "7":
            return int("Error")
        else:
            binary += bin(int(num_permission[index]))

        index += 1

    # Removes the "0b" prefix bin() adds TODO: Refactor with RegEx?
    binary = list(binary)
    # print(binary)   # NOTE: Debug
    del binary[0]
    del binary[0]
    del binary[3]
    del binary[3]
    del binary[6]
    del binary[6]
    binary = "".join(binary)

    sym_permission = ""
    index = 0

    # Adds 0's until binary is 9 length
    while len(binary) != 9:
        binary += "0"

    # Converts binary to symbolic permission
    for num_permission in binary:
        if num_permission == '1':
            if index == 0 or index == 3 or index == 6:
                sym_permission += "r"
            elif index == 1 or index == 4 or index == 7:
                sym_permission += "w"
            else:
                sym_permission += "x"
        else:
            sym_permission += "-"

        index += 1

    return sym_permission


# Max permission is rwxrwxrwx min permission is ---------
def validate_permission(permission):
    if permission.isdigit():
        if len(permission) != 3:
            return int("Error")

    else:
        if len(permission) != 9:
            return int("Error")

        r = [permission[0], permission[3], permission[6]]
        w = [permission[1], permission[4], permission[7]]
        x = [permission[2], permission[5], permission[8]]

        for index in r:
            if index == "r" or index == "-":
                continue
            else:
                return int("Error")

        for index in w:
            if index == "w" or index == "-":
                continue
            else:
                return int("Error")

        for index in x:
            if index == "x" or index == "-":
                continue
            else:
                return int("Error")

    return True


# Menu loop
def main():
    while True:
        try:
            print("\n-MENU-")
            choice = int(input("1: Symbolic to numeric\n"
                               "2: Numeric to symbolic\n"
                               "3: Exit\n"))

            if choice not in Menu.RANGE.value:
                int("Error")

            elif choice == Menu.SYM2NUM.value:
                permission = input("\nEnter the symbolic permission " +
                                   "you want (ex. rw-r--r--): ")

                if validate_permission(permission):
                    print("The corresponding numeric permission is: " +
                          symbolic_to_numeric(permission))

            elif choice == Menu.NUM2SYM.value:
                permission = input("\nEnter the numeric permission " +
                                   "you want (ex. 775): ")

                if validate_permission(permission):
                    print("The corresponding symbolic permission is: " +
                          numeric_to_symbolic(permission))

            elif choice == Menu.EXIT.value:
                break
        except ValueError:
            print(Menu.ERROR.value)

if __name__ == '__main__':
    main()
