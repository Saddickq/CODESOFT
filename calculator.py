#!/usr/bin/python3

class Calculator:
    def __init__(self, num1, opt, num2):
        if not isinstance(num1, int):
            raise TypeError("Numbers must be an integer")
        self.__num1 = num1
        
        self.__opt = opt
        
        if not isinstance(num2, int):
            raise TypeError("Numbers must be an integer")
        self.__num2 = num2
    
    def calculate(self):
        if self.__opt == '+':
            result = self.__num1 + self.__num2
        elif self.__opt == '-':
            result = self.__num1 - self.__num2
        elif self.__opt == '*':
            result = self.__num1 * self.__num2
        elif self.__opt == '/':
            if self.__num2 == 0:
                raise ZeroDivisionError("Division by zero is incorrect")
            result = self.__num1 / self.__num2
        else:
            raise ValueError("Invalid operation")

        return result

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 4:
        print('<Usage>: <num1> <operation> <num2>')
        print('For multiplication add a backslash to operator <\*>')
    else:
        try:
            calculate = Calculator(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
            print(calculate.calculate())
        except (ValueError, TypeError, ZeroDivisionError) as err:
            print(err)