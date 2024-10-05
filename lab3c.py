#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''

# Author ID: [124876228]

def describe_temperature(temp):

    if temp > 30:

        return 'hot'

    elif temp < 0:

        return 'cold'

    elif temp == 20:

        return 'perfect'

    return 'ok'

if __name__ == '__main__':

    print(describe_temperature(50))    # Should return 'hot'

    print(describe_temperature(20))    # Should return 'perfect'

    print(describe_temperature(-50))   # Should return 'cold'

    print(describe_temperature(25))    # Should return 'ok'

    print(describe_temperature(10))    # Should return 'ok'

def operate(number1, number2, operator):

    if operator == 'add':

        return number1 + number2

    elif operator == 'subtract':

        return number1 - number2

    elif operator == 'multiply':

        return number1 * number2

    return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':

    print(operate(10, 5, 'add'))        

    print(operate(10, 5, 'subtract'))   

    print(operate(10, 5, 'multiply'))   

    print(operate(10, 5, 'divide'))     




