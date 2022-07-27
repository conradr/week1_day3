def return_10():
    return 10


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def length_of_string(test_string):
    return len(test_string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(num1, num2):
    intNum1 = int(num1)
    intNum2 = int(num2)
    return intNum1 + intNum2

def number_to_full_month_name(month):
    calendar = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    return calendar[month]

def number_to_short_month_name(month):
    shortMonth = number_to_full_month_name(month)
    return shortMonth[0:3]

def volume_of_cube(length):
    return length**3

def reverse_string(string):
    return string[::-1]

def conversion(temp):
    return (temp - 32) / 1.8

